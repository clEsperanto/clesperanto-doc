Installation
============

From package managers (Recommmended)
-------------------------------------

pyclesperanto is available on PyPI and conda-forge. We recommend installing it from one of these package managers.

Install from conda-forge with `conda` or `mamba`:

.. tab:: Pip

    Install from PyPI with `pip`:

    .. code:: bash

        pip install pyclesperanto

.. tab:: Conda

    Install from conda-forge with `conda` or `mamba`:

    .. code:: bash

        conda install -c conda-forge pyclesperanto



.. important::

    Installing pyclesperanto with mamba or conda on MacOS or Linux will require an additional package to be installed to see compatible OpenCL platforms.

    .. tab:: MacOS

        .. code:: bash

            conda install -c conda-forge ocl_icd_wrapper_apple

    .. tab:: Linux

        .. code:: bash

            conda install -c conda-forge ocl-icd-system

.. tip::

    It is strongly advised to install pyclesperanto in a virtual environment. For example, you can create a new environment with conda:

    .. code:: bash

        conda create -n myenv
        conda activate myenv

From source
-----------

For Development, or if you are using a platform not supported by the package managers, you can install pyclesperanto from source. 
This process will requires you to have a C compiler available on your system. 
Similarly to installing pyclesperanto from the package managers, it is recommended to install it in a virtual environment.

Clone the repository using ``git`` and install it with ``pip``. The installation can take a few minutes to complete.

.. code:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto
    pip install -e .

.. tip::

    You can add the flag ``-v`` to enable verbose output of the build process. This is particularly useful for debugging and provid building logs when reporting issues.



