Installation
============

From package managers (Recommended)
-----------------------------------

We recommend installing with `pixi` but you can also install with `pip` or `conda` based on your preference and platform.
By default, pyclesperanto will come with `OpenCL` as a backend but other backends are available as optional dependencies. 
For simplicity, we recommand installing pyclesperanto with all possible backends with the option `[all]` or specific backends like `CUDA` with the option `[cuda]`. 

Installation options are as follows:
- `[cuda]`: Install pyclesperanto with Opencl and CUDA backend (not compatible with macOS).
- `[metal]`: Install pyclesperanto with OpenCL and Metal backend (only compatible with macOS).
- `[all]`: Install pyclesperanto with all available backends (OpenCL, CUDA, Metal) that are compatible with your system.

.. tab:: Pixi (Recommended)

    Install from pixi with `pixi`:

    .. code:: bash

        pixi add --pypi pyclesperanto[all]

    .. note::

        For `zsh` users, like on `MacOS`, you may need to quote the package name to prevent shell expansion of the square brackets: `pyclesperanto[all]` should be written as ``'pyclesperanto[all]'`` or ``"pyclesperanto[all]"``.

.. tab:: Pip

    Install from PyPI with `pip`:

    .. code:: bash

        pip install pyclesperanto[all]

    .. note::

        For `zsh` users, like on `MacOS`, you may need to quote the package name to prevent shell expansion of the square brackets: `pyclesperanto[all]` should be written as ``'pyclesperanto[all]'`` or ``"pyclesperanto[all]"``.

.. tab:: Conda/Mamba (Degraded)

    Install from conda-forge with `conda` or `mamba`. Options for installing with specific backends are not available with conda, it is necessary to install backend specific packages separately along with the main package. 

    .. code:: bash

        conda install -c conda-forge pyclesperanto pyclesperanto-opencl

    .. note::

        Add the following packages to install the CUDA and Metal backends:
        - For CUDA backend: `pyclesperanto-cuda` (not compatible with macOS).
        - For Metal backend: `pyclesperanto-metal` (only compatible with macOS).

    .. important::

        Installing pyclesperanto with mamba or conda on MacOS or Linux will require an additional package to be installed to see compatible OpenCL platforms.

        .. tab:: MacOS

            .. code:: bash

                conda install -c conda-forge ocl_icd_wrapper_apple

        .. tab:: Linux

            .. code:: bash

                conda install -c conda-forge ocl-icd-system


.. tip::

    It is strongly advised to install pyclesperanto in a virtual environment.  
    We recommend using `pixi` for a local and project specific installation, but you can also use `venv` or `conda` to create a virtual environment before installing pyclesperanto.

.. important::

    Installing a backend does not guarantee that it will work on your system (e.g. `CUDA`` may be install on a linux system but not work if there is no NVIDIA GPU available). 


From source
-----------

If you want to try the latest development version of pyclesperanto or if existing wheel does not cover your platform (e.g. Arch Linux) or desired configuration.

First, `git clone` the repository

.. code:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto

Then, you can install pyclesperanto with `pixi` or `pip`:

.. tab:: Pixi (Recommended)

    Inside the cloned repository, install pyclesperanto environment with `pixi`:

    .. code:: bash

        pixi install

    then build and test the OpenCL backend:

    .. code:: bash

        pixi run build-ocl
        pixi run test-ocl

    Or other `pixi` commands are available to build specific backends, for example:

    .. code:: bash

        pixi run build-cuda
        pixi run test-cuda

.. tab:: Pip

    You can also build and install pyclesperanto with `pip`. First, you will need to build the backends you which to use:

    .. code:: bash

        pip install -e ./backend/opencl -v
        pip install -e ./backend/cuda -v

    Then, you can install the main package:

    .. code:: bash

        pip install -e . -v

    You can run the tests with `pytest` on all the available backends or specific backends with the option `-k`:

    .. code:: bash

        pytest -v
        pytest -v -k ocl
        pytest -v -k cuda

.. note::

    Installing from source is particularly useful if you want to contribute to the package, or if you want to use the package on a non-supported platform (e.g. like Arch Linux)


Troubleshooting
---------------

If you encounter issues during installation or usage that you cannot resolve or consider them bugs, please report them on the `GitHub Issues page <https://github.com/clEsperanto/pyclesperanto/issues>`__.
