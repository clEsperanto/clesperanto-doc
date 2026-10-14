Installation
============

From package managers (Recommended)
-----------------------------------

By default, pyclesperanto comes with ``OpenCL`` as a backend, but other backends are available as optional dependencies. 

Installation options are as follows:

.. list-table::
   :widths: 20 80

   * - ``[cuda]``
     - Provides OpenCL and CUDA backend (not compatible with macOS).
   * - ``[metal]``
     - Provides OpenCL and Metal backend (only compatible with macOS).
   * - ``[all]``
     - Provides all available backends for your system.

For simplicity, we recommend installing pyclesperanto with all available backends using the ``[all]`` option, or specific backends like CUDA using the ``[cuda]`` option. 

.. tab:: Pip

    Install from PyPI with ``pip``:

    .. code:: bash

        pip install pyclesperanto[all]

    .. note::

        For ``zsh`` users (such as on macOS), you may need to quote the package name to prevent shell expansion of square brackets: ``pyclesperanto[all]`` should be written as ``'pyclesperanto[all]'`` or ``"pyclesperanto[all]"``.

.. tab:: Conda/Mamba (Degraded)

    **WIP**: The conda-forge package is currently in a degraded state and may not work properly. We recommend using pip for installation instead.


.. tip::

    It is strongly advised to install pyclesperanto in a virtual environment.
    We recommend using ``pixi`` for a local, project-specific installation, but you can also use ``venv`` or ``conda`` to create a virtual environment.

.. important::

    Installing a backend does not guarantee that it will work on your system. e.g. the ``CUDA`` backend can be installed on a Linux system but may not work if you do not have an NVIDIA GPU available. 


From source
-----------

If you want to try the latest development version of pyclesperanto, if an existing wheel does not cover your platform (e.g., Arch Linux), or if you which to contribute to the project, you can build pyclesperanto from source.

First, clone the repository using ``git``:

.. code:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto

We provide a ``pixi.toml`` file to facilitate building and testing with ``pixi``, but you can also build and test with ``pip`` if you prefer.

.. tab:: Pixi (Recommended)

    Inside the cloned repository, install the pyclesperanto environment with ``pixi``:

    .. code:: bash

        pixi install

    Then, build and test the OpenCL backend:

    .. code:: bash

        pixi run build-ocl
        pixi run test-ocl

    Other ``pixi`` commands are available to build specific backends. For example:

    .. code:: bash

        pixi run build-cuda
        pixi run test-cuda

.. tab:: Pip

    You can also build and install pyclesperanto with ``pip``. First, build the backends you wish to use:

    .. code:: bash

        pip install -e ./backend/opencl -v
        pip install -e ./backend/cuda -v

    Then, you can install the main package:

    .. code:: bash

        pip install -e . -v

    You can run the tests with ``pytest`` on all available backends or on specific backends using the ``-k`` option:

    .. code:: bash

        pytest -v
        pytest -v -k ocl
        pytest -v -k cuda


Troubleshooting
---------------

If you encounter issues during installation or usage, please report them on the `GitHub Issues page <https://github.com/clEsperanto/pyclesperanto/issues>`__.
