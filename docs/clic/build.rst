Library compilation
===================

Requirements
------------

Here are the software required for building the C++ CLIc library.
If you never compiled a C++ project before, you may want to check out these tutorials before proceeding:

- `C++ Tutorial <https://www.tutorialspoint.com/cplusplus/index.htm>`__.
- `CMake Tutorial <https://cmake.org/cmake/help/latest/guide/tutorial/index.html>`__.

Otherwise, you'll need the following software to continue:

- `Git <https://git-scm.com/downloads>`__
- `CMake <https://cmake.org/download/>`__ (version 3.20 or higher)
- `OpenCL <https://www.khronos.org/opencl/>`__ (usually provided by the GPU vendor)
- `Python <https://www.python.org/downloads/>`__
- a C++ Compiler:
    - On Windows, you can install it with `MSVC <https://visualstudio.microsoft.com/>`__
    - On macOS, you can install the `Xcode command line tools <https://developer.apple.com/xcode/resources/>`__
    - On Linux, you can install GCC with the `build-essential <https://packages.ubuntu.com/jammy/build-essential>`__ package.
    - Or any other compiler that supports C++17 should work.

.. important::

   Ensure that all the following software are available in your system's ``$PATH`` variable, especially `Git` and `CMake`.
   Please, refer to the respective software documentation for installation instructions and usage.

Building the project
--------------------

.. tab:: Using VSCode   

    - From VSCode, git clone the repository ``Ctrl+Shift+P -> Git: clone``
    - Install the `C/C++ Extension Pack` provided by Microsoft. 
    - Configure the project build using the CMake side menu.
        - Select a configuration process (``Ninja ...``, ``MSVC ...``, ``Makefile ...``, etc.)
        - Select a build type (``Debug``, ``Release``, etc.)
        - (Optional) Select a build test type (``Debug``, ``Release``, etc.)
    - Run the configuration process ``Ctrl+Shift+P -> CMake: Configure``
    - Build the project using CMake ``Ctrl+Shift+P -> CMake: Build``

    .. important::

        Tests in ``Release`` mode will always pass. For a proper test run, you should build them in ``Debug`` mode.

    .. seealso::

        VSCode Documentation for C++ project: https://code.visualstudio.com/docs/cpp/introvideos-cpp



.. tab:: Using Terminal CLI
    
    In a terminal, make sure that you have ``cmake`` and ``git`` command available by running the following commands.
    They should return the version of the software without any error message. 
    
    .. code-block:: bash

        git --version
        cmake --version

    We can start by cloning the repository with Git from github.

    .. code-block:: bash

        git clone https://github.com/clEsperanto/CLIc.git
        cd CLIc

    Inside the cloned repository, we can use CMake's command-line interface to configure the project.  

    .. code-block:: bash

        cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=ON

    The parameter ``-S`` specifies the source directory and ``-B`` specifies the build directory. ``-G`` allows you to specify your project generator like `Ninja`, `MSVC`, `XCode`, or other compatible with CMake.
    The choice of the generator depends on your system and your preference. 
    Finally, You can also provide additional configuration input to the project by adding addition parameter as followed ``-D<NAME_OF_THE_VARIABLE>=<VALUE>``. 
    In this example, we are setting the build type to ``Release`` and asking CMake to also build the library tests.

    Once configure, we can build the project with the following command:

    .. code-block:: bash

        cmake --build build --parallel 10 --target install

    This command will build the project in parallel using 10 threads and install the project in the system.

    .. note::

        By default the installation directory follows a GNU standard, which is usually ``/usr/local`` for Unix system.
        If you want to change the installation directory, you can set the variable ``CMAKE_INSTALL_PREFIX`` during the configuration step.
        This allows you to better control where the library and headers are installed.    


.. tab:: Using CMake GUI

    If you prefer a graphical interface, you can use CMake's GUI. The logic is the same as the command-line interface, but you can set the variables in the GUI.

    1. Open CMake GUI
    2. Set the source directory to the path where you cloned the repository.
    3. Set the build directory to a path where you want to build the project.
    4. Click on ``Configure`` and select your compiler/generator.
    5. Set the variables you want to change.
    6. Click on ``Generate``.

    Once you have generated the project, you can open the project file with your IDE (this should match the compiler/generator you have selected in the GUI) and build the project.



CMake Configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following options are available:

- :BUILD_TESTS: Enable the build of the tests. Default is ``OFF``.
- :BUILD_CUDA_BACKEND: Enable the build of the CUDA backend. Default is ``OFF``.
- :BUILD_OPENCL_BACKEND: Enable the build of the OpenCL backend. Default is ``ON``.
- :BUILD_DOCUMENTATION: Enable the build of the documentation. Default is ``ON`` (``sphinx`` and ``doxygen`` required, else it will be skipped).
- :BUILD_SHARED_LIBS: Build the library as a shared library. Default is ``ON``.
- :BUILD_COVERAGE: Enable the build of the coverage report. Default is ``OFF``.
- :BUILD_BENCHMARKS: Enable the build of the benchmarks. Default is ``OFF`` (Work in Progress).
- :CMAKE_BUILD_TYPE: Specify the build type. Possible values are ``Debug``, ``Release``, ``RelWithDebInfo``, ``MinSizeRel``.
- :CMAKE_INSTALL_PREFIX: Specify the installation directory. Default is ``/usr/local``.

Running the Tests
-----------------

Simply building the library does not necessarily guarantee its correct functionality. Tests provided with the library must be run to ensure that the library is working as expected.

If the option ``-D BUILD_TESTS=ON`` is set during configuration (it is by default) the tests will be built along with the library and can be run.

Once built, one can run all the tests using the following command in the build directory:

.. code-block:: bash

   ctest --test-dir ./build -C Debug -V

The ``--test-dir`` flag specifies the directory where the build is located. The ``-C`` flag specifies the configuration to use.
The ``-V`` flag indicates that the tests should be run in verbose mode.

.. note::

  If built traditionally, the root directory of the build should be ``./build/{config_type_build}/``, where ``{config_type_build}`` depends on the system and configuration used, e.g., ``./build/linux-ninja-multi/`` for Ubuntu systems.

.. hint::

  It is also possible to run a particular test using the ``ctest`` command: ``ctest --test-dir ./build -C Debug -R {test_name}``.

If using VSCode or any other IDE, it is also possible to run the tests directly from it. Please refer to the respective software documentation for instructions on how to run the tests with CMake and the IDE.


