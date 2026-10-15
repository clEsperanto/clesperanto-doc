Pyclesperanto on HPC
====================

This is a minimal example of how to run a Python script that uses ``pyclesperanto`` (OpenCL or CUDA backend) on a SLURM cluster. It reflects our hardware/software setup and may need adapting to your cluster.

Setup
-----

For this example, we rely on `pixi <https://pixi.sh>`__ and `Apptainer <https://apptainer.org>`__ for deployment: a pixi environment containing ``pyclesperanto[opencl]`` or ``pyclesperanto[cuda]`` is packaged in an Apptainer image (``pixi.sif``).

The two backends have different requirements on a cluster, so each one is run in its **own** ``apptainer exec`` call (see `Never mix both backends`_).

Common rules
------------

- Always use ``apptainer exec --cleanenv --nv``.

  - ``--nv`` injects the host NVIDIA driver libraries (``libcuda.so``, ``libnvidia-opencl.so``, ...).
  - ``--cleanenv`` keeps the host environment (modules, ``LD_LIBRARY_PATH``, ``CUDA_HOME``, ...) out of the container.

- Forward ``CUDA_VISIBLE_DEVICES`` with ``--env``, otherwise ``--cleanenv`` drops the GPU assigned by SLURM.
- Do not ``module load cuda``: the wheels bring their own CUDA runtime. A host module puts a stub ``libcuda.so`` on ``LD_LIBRARY_PATH`` that shadows the real driver and breaks PTX loading.
- Check the node's driver with ``nvidia-smi``.

CUDA backend
------------

``pyclesperanto[cuda]`` bundles CUDA 12.6 (runtime and nvrtc). If the cluster driver only supports an older CUDA (e.g. 535.183.01 / CUDA 12.2), kernels fail to load (``CUDA_ERROR_UNSUPPORTED_PTX_VERSION``, ``CUDA_ERROR_INVALID_PTX``). The fix is the NVIDIA `forward-compatibility <https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html>`__ libraries:

.. important::

    For more recent CUDA versions (13.0 and above), please open an issue on `GitHub <https://github.com/clEsperanto/pyclesperanto/issues>`__ for support. We will try to provide a wheel with a newer CUDA runtime.

1. Download the ``cuda-compat-12-6`` ``.deb`` package from `NVIDIA's CUDA repository <https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/>`__ (match the CUDA version bundled in the wheel), e.g. ``wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-compat-12-6_560.35.05-0ubuntu1_amd64.deb``.
2. Extract it without root: ``dpkg-deb -x cuda-compat-12-6_*.deb cuda-compat-12-6/``.
3. Use the directory holding the compat ``libcuda.so*`` (typically ``usr/local/cuda-12.6/compat``) as ``CUDA_COMPAT_DIR``.
4. Bind it read-only and set ``LD_LIBRARY_PATH`` to it, **for the CUDA process only**.

Limits: forward compatibility only works on data-center GPUs (A100, H100, ...). If your driver already supports CUDA 12.6, skip the compat libraries. For newer CUDA versions, open an issue on `GitHub <https://github.com/clEsperanto/pyclesperanto/issues>`__.

SBATCH example
~~~~~~~~~~~~~~

.. code:: bash

    #!/bin/bash
    #SBATCH --job-name=pyclesperanto
    #SBATCH --output=slurm_%j.out
    #SBATCH --error=slurm_%j.err
    #SBATCH --partition=g
    #SBATCH --gres=gpu:1
    #SBATCH --cpus-per-task=2
    #SBATCH --mem=10G
    #SBATCH --time=01:00:00

    CONTAINER=$HOME/pixi.sif
    CUDA_COMPAT_DIR="$HOME/cuda-compat-12-6"

    # No host CUDA module / library path leaking into the container
    module unload cuda 2>/dev/null || true
    unset CUDA_HOME CUDA_PATH CUDA_ROOT LD_LIBRARY_PATH

    apptainer exec --cleanenv --nv \
        --env "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-}" \
        --env "LD_LIBRARY_PATH=${CUDA_COMPAT_DIR}" \
        --bind "$PWD:$PWD,$CUDA_COMPAT_DIR:$CUDA_COMPAT_DIR:ro" \
        --pwd $PWD "$CONTAINER" pixi run python my_cuda_script.py

OpenCL backend
--------------

- The OpenCL ICD loader must find the vendor ICDs (``nvidia.icd``). ``--nv`` does not provide them, so bind ``/etc/OpenCL/vendors`` (check the path exists on the compute node).
- Do **not** bind the compat libraries nor set ``LD_LIBRARY_PATH``: the compat package replaces ``libcuda.so`` but not ``libnvidia-opencl.so``, so OpenCL must use the real host driver libraries.

SBATCH example
~~~~~~~~~~~~~~

.. code:: bash

    #!/bin/bash
    #SBATCH --job-name=pyclesperanto
    #SBATCH --output=slurm_%j.out
    #SBATCH --error=slurm_%j.err
    #SBATCH --partition=g
    #SBATCH --gres=gpu:1            # or a specific model, e.g. gpu:A100:1
    #SBATCH --cpus-per-task=2
    #SBATCH --mem=10G
    #SBATCH --time=01:00:00

    CONTAINER=$HOME/pixi.sif

    # Bind the host's OpenCL ICD registry so the NVIDIA platform is discoverable
    APPTAINER_BINDS="$PWD:$PWD"
    if [ -d /etc/OpenCL/vendors ]; then
        APPTAINER_BINDS="$APPTAINER_BINDS,/etc/OpenCL/vendors:/etc/OpenCL/vendors"
    fi

    apptainer exec --cleanenv --nv \
        --env "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-}" \
        --bind "$APPTAINER_BINDS" --pwd $PWD "$CONTAINER" pixi run python my_opencl_script.py

Submit with ``sbatch my_job.sh``.

.. _never-mix-backends:

Never mix both backends
-----------------------

If CUDA (with the compat ``libcuda.so``) and OpenCL are used in the **same process**, the compat ``libcuda.so`` is loaded first and the OpenCL ICD (built against the host driver) reuses it instead of its matching sibling. This version-skewed pairing works on small buffers but hangs or crashes on large ones. Use one ``apptainer exec`` per backend, with the compat directory only for the CUDA one. A job needing both is simply two sequential calls.

Troubleshooting
---------------

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Symptom
      - Likely cause / fix
    * - ``CUDA_ERROR_UNSUPPORTED_PTX_VERSION``, ``CUDA_ERROR_INVALID_PTX``, "driver version is insufficient"
      - Driver older than bundled CUDA: use forward compatibility.
    * - Same errors even with compat libs
      - A host CUDA module or ``LD_LIBRARY_PATH`` leaks a stub ``libcuda.so``: use ``--cleanenv``, unload the module.
    * - 0 CUDA devices visible
      - Check ``--gres``, ``--nv``, and that ``CUDA_VISIBLE_DEVICES`` is forwarded with ``--env``.
    * - No OpenCL platform (``CL_PLATFORM_NOT_FOUND_KHR``) while ``nvidia-smi`` works
      - ICDs not visible: bind ``/etc/OpenCL/vendors``.
    * - OpenCL works on small buffers, hangs or kills the job on large ones
      - Compat ``libcuda.so`` loaded in the OpenCL process: see `Never mix both backends`_.
