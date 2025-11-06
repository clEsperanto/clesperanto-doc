Installation
============

From package managers (Recommended)
-----------------------------------

pyclesperanto is available on PyPI and conda-forge. We recommend installing it from one of these package managers.

.. tab:: Pip

    Install from PyPI with `pip`:

    .. code:: bash

        pip install pyclesperanto

.. tab:: Pixi

    Install from pixi with `pixi`:

    .. code:: bash

        pixi add --pypi pyclesperanto

    .. note::

        It is recommended to use --pypi flag to ensure installation from PyPI repository with `pixi`.

.. tab:: Conda/Mamba

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

    It is strongly advised to install pyclesperanto in a virtual environment.  
    For example, you can create a new environment with `conda`:

    .. code:: bash

        conda create -n myenv
        conda activate myenv


From source
-----------

If you want to try the latest development version of pyclesperanto or if existing wheel does not cover your platform (e.g. Arch Linux) or desired configuration.
Similarly to classic installation, we advise to install it in a virtual environment.

From the repository
~~~~~~~~~~~~~~~~~~~

you can install it directly from the GitHub repository using pip.

.. code:: bash

    pip install git+https://github.com/clEsperanto/pyclesperanto.git

For Development
~~~~~~~~~~~~~~~

For Development or Custom Builds you will need to download the source code and build it locally.
Clone the repository using ``git`` and install it with ``pip``. The installation can take a few minutes to complete.

.. code:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto
    pip install -e .

.. tip::

    You can add the flag ``-v`` to enable verbose output of the build process. This is particularly useful for debugging and providing build logs when reporting issues.

.. note::

    Installing from source is particularly useful if you want to contribute to the package, or if you want to use the package on a non-supported platform (e.g. like Arch Linux)


Pyclesperanto rely on a continuous integration system to automatically build and test the package on multiple platforms and python versions.
Tests can be run locally using ``pytest``:

.. code:: bash

    pytest -v


Troubleshooting
---------------

If you encounter issues during installation or usage that you cannot resolve or consider them bugs, please report them on the `GitHub Issues page <https://github.com/clEsperanto/pyclesperanto/issues>`__.
