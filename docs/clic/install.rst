Installation
============

CLIc is a C++ library that requires compilation before use. This guide will help you set up your environment and build the library from source.
If you are new to C++ development, you may want to familiarize yourself with C++ and CMake before proceeding. 

- `C++ Tutorial <https://www.tutorialspoint.com/cplusplus/index.htm>`__.
- `CMake Tutorial <https://cmake.org/cmake/help/latest/guide/tutorial/index.html>`__.

Requirements
------------

You'll need the following software installed on your system:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Software
     - Minimum Version
     - Purpose & Installation
   * - Git
     - Latest
     - Version control for cloning the repository. `Download <https://git-scm.com/downloads>`__
   * - CMake
     - 3.20+
     - Build system generator. `Download <https://cmake.org/download/>`__
   * - C++ Compiler
     - C++17 compatible
     - **Windows**: `MSVC <https://visualstudio.microsoft.com/>`__ or Visual Studio Build Tools | **macOS**: `Xcode command line tools <https://developer.apple.com/xcode/resources/>`__ (``xcode-select --install``) | **Linux**: `GCC <https://packages.ubuntu.com/jammy/build-essential>`__ or Clang
   * - OpenCL
     - Latest
     - GPU compute framework. Usually provided by your `GPU vendor <https://www.khronos.org/opencl/>`__
   * - Python
     - 3.6+
     - Build tool support. Usually included with your OS. `Download <https://www.python.org/downloads/>`__

**Quick Verification**: Open a terminal and run these commands to verify your setup:

.. code-block:: bash

    git --version              # Check Git installation
    cmake --version            # Check CMake installation
    python --version           # Check Python installation

.. important::

   Ensure that all the following software are available in your system's ``$PATH`` variable, especially `Git` and `CMake`.
   Please refer to the respective software documentation for proper installation instructions.


Building the library
--------------------


.. tab:: VSCode

    - Install the `C/C++ Extension Pack` Extension provided by Microsoft.

    .. container:: figure-centered
        
        .. figure:: ./image/cpp_vscode_extention.png
            :alt: C/C++ Extension Pack installation
            :width: 50%

    - Git clone the repository ``Ctrl+Shift+P -> Git: clone`` and provide the repository URL: ``https://github.com/clEsperanto/CLIc.git``

    .. container:: figure-centered
        
        .. figure:: ./image/git_clone_clic.png
            :alt: Git clone CLIc repository
            :width: 80%

    - The project comes with pre-configured CMake settings for ``MSVC``, ``Ninja`` and ``Makefile``.
        - Open the CMake Tools side panel from the left toolbar
        - Select a configuration process (``Ninja ...``, ``MSVC ...``, ``Makefile ...``, etc.) depending on your system and preference.

        .. container:: figures-grid

            .. figure:: ./image/cmake_tool_panel.png
                :width: 95%
                :alt: Install C++ Extension Pack

                **Step 1:** Open CMake Tools Menu

            .. figure:: ./image/select_preset.png
                :width: 95%
                :alt: CMake configuration

                **Step 2:** Select a configuration   

        - Select a build type (``Debug``, ``Release``, etc.)

        .. container:: figure-centered
        
            .. figure:: ./image/build_type.png
                :alt: CMake build type selection
                :width: 80%

        - Run the configuration and build process ``Ctrl+Shift+P -> CMake: Configure`` and then ``Ctrl+Shift+P -> CMake: Build``

        .. container:: figure-centered

            .. figure:: ./image/config_build.png
                :alt: CMake build process
                :width: 80%

    .. seealso::

        VSCode Documentation for C++ project: https://code.visualstudio.com/docs/cpp/introvideos-cpp

.. tab:: CLI Terminal

    Prerequisites Check
    ~~~~~~~~~~~~~~~~~~~

    Before you begin, verify that you have ``cmake`` and ``git`` installed on your system.
    Open a terminal and run the following commands to check their availability:

    .. code-block:: bash

        git --version
        cmake --version

    Both commands should return version information without any error messages.
    
    Cloning the Repository
    ~~~~~~~~~~~~~~~~~~~~~~

    Start by cloning the CLIc repository from GitHub using Git:

    .. code-block:: bash

        git clone https://github.com/clEsperanto/CLIc.git
        cd CLIc

    This creates a new directory called ``CLIc`` and navigates into it.

    Configuring the Project
    ~~~~~~~~~~~~~~~~~~~~~~~

    Inside the cloned repository, use CMake to configure the project.
    The basic command structure is:

    .. code-block:: bash

        cmake -S . -B build -G <Generator> -DCMAKE_BUILD_TYPE=<BuildType> [OPTIONS]

    **Parameters:**

    - ``-S .`` - Specifies the source directory (current directory)
    - ``-B build`` - Specifies the build directory where generated files will be placed
    - ``-G <Generator>`` - Specifies the build system generator (e.g., ``Ninja``, ``Unix Makefiles``, ``Visual Studio 17 2022``, etc.), list of generators can be found in the `CMake documentation <https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html>`__
    - ``-DCMAKE_BUILD_TYPE=<BuildType>`` - Specifies the build type: ``Debug``, ``Release``, ``RelWithDebInfo``, or ``MinSizeRel``
    - ``[OPTIONS]`` - Additional CMake variables using the ``-D<NAME>=<VALUE>`` format

    Building the Project
    ~~~~~~~~~~~~~~~~~~~~

    Once the project is configured, build it using:

    .. code-block:: bash

        cmake --build build --parallel <num_threads>

    **Parameters:**

    - ``--build build`` - Specifies the build directory
    - ``--parallel <num_threads>`` - Builds using multiple threads for faster compilation (e.g., ``10``)


.. tab:: CMake GUI

    Setting Up the Build Directory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Start by launching the CMake GUI application from your system interface or from the terminal by running ``cmake-gui``.
    Once CMake GUI is open, you need to configure the source and build directories:

    1. **Source Code Path**: Click ``Browse Source`` and navigate to the cloned CLIc repository directory.

    2. **Build Path**: Click ``Browse Build`` and create or select a build directory (e.g., ``CLIc/build``).

    .. container:: figure-centered
        
        .. figure:: ./image/cmake_gui.png
            :alt: CMake GUI source and build path configuration
            :width: 80%

    .. note::

        It is recommended to create a separate ``build`` directory inside the project directory to keep the source code clean.

    Configuring the Project
    ~~~~~~~~~~~~~~~~~~~~~~~

    After setting the paths, follow these steps:

    1. Click the ``Configure`` button.

    2. A dialog box will appear asking you to select the generator (build system).
       Choose the generator that matches your system and preference:
       
       - On Windows: ``Visual Studio 17 2022``, ``Ninja``, or ``Unix Makefiles``
       - On macOS: ``Xcode``, ``Ninja``, or ``Unix Makefiles``
       - On Linux: ``Unix Makefiles`` or ``Ninja``

    .. container:: figures-grid

        .. figure:: ./image/cmake_generator.png
            :width: 95%
            :alt: Generator selection dialog

            **Step 1:** Select the generator

        .. figure:: ./image/cmake_generator_list.png
            :width: 95%
            :alt: Generator list

            **Step 2:** Select the generator from the list (present on your system)

    3. After selection, CMake will analyze the project and populate the configuration options. 

    .. note::

        Similarly to VSCode, CMake GUI can load and use the pre-configured presets located in the ``cmake/presets`` directory of the project.

    Fix Requirements and set Options
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    After configuration is complete, you will see a list of CMake variables in the CMake GUI window. They represent various build options, settings, and dependencies.
    Configure again to validate the settings and ensure all dependencies are met, until no red entries remain.

    Fields are highlighted in red that remains indicates missing dependencies or information that need to be resolved before proceeding (e.g. cmake could not find OpenCL headers).
    This is usually fixed by installing the missing dependencies on your system or providing the correct paths to CMake.

    .. container:: figures-grid

        .. figure:: ./image/cmake_configuration_1.png
            :width: 95%
            :alt: First configuration run

            **Step 1:** First configuration run, with unvalidated settings in red

        .. figure:: ./image/cmake_configuration_2.png
            :width: 95%
            :alt: Second configuration run to validate settings

            **Step 2:** Second configuration run to validate settings

    **Common options to configure:**

    - ``BUILD_TESTS``: Set to ``ON`` to build the tests
    - ``CMAKE_BUILD_TYPE``: Select ``Debug``, ``Release``, etc.

    Building the Project
    ~~~~~~~~~~~~~~~~~~~~

    Once you have configured all the options, we can generate the build files accordingly to your generator choice.

    1. Click the ``Generate`` button to generate the build files.

    2. After successful generation, a message will appear at the bottom of the window confirming the build files were created.

    3. The final build step will depend on the selected generator. Makefiles and Ninja can be built from the command line, while Visual Studio and Xcode projects can be opened directly.

    .. container:: figure-centered
        
        .. figure:: ./image/cmake_xcode.png
            :alt: XCode project after generation
            :width: 80%

    Troubleshooting
    ~~~~~~~~~~~~~~~

    - **Red entries in the configuration list**: These indicate errors or missing dependencies. 
      Hover over them to see detailed error messages and install any missing software or indicate the correct paths to them.
    
    - **Generator not available**: Ensure you have the chosen generator properly installed, CMake compatible generator can be found in its `documentation <https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html>`__.

    - **Path issues**: Make sure all required libraries and software are in your system ``PATH``.

    .. seealso::

        CMake GUI Documentation: https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html


CMake Configuration options Project Variables
---------------------------------------------

The following options are available:

- :BUILD_TESTS: Enable the build of the tests. Default is ``OFF``.
- :BUILD_CUDA_BACKEND: Enable the build of the CUDA backend. Default is ``OFF``, (__WIP__).
- :BUILD_OPENCL_BACKEND: Enable the build of the OpenCL backend. Default is ``ON``.
- :BUILD_DOCUMENTATION: Enable the build of the documentation. Default is ``ON`` (``sphinx`` and ``doxygen`` required, else it will be skipped).
- :BUILD_SHARED_LIBS: Build the library as a shared library. Default is ``ON``.
- :BUILD_COVERAGE: Enable the build of the coverage report. Default is ``OFF``.
- :BUILD_BENCHMARKS: Enable the build of the benchmarks. Default is ``OFF`` (__WIP__).
- :CMAKE_BUILD_TYPE: Specify the build type. Possible values are ``Debug``, ``Release``, ``RelWithDebInfo``, ``MinSizeRel``.
- :CMAKE_INSTALL_PREFIX: Specify the installation directory. Default is ``/usr/local``.


Running the Tests
-----------------

Simply building the library does not necessarily guarantee its correct functionality. Tests provided with the library must be run to ensure that the library is working as expected.
If the option ``-D BUILD_TESTS=ON`` is set during configuration (it is by default), the tests will be built along with the library and can be run.
Once built, one can run all the tests using the following command in the build directory:

.. code-block:: bash

   ctest --test-dir ./build -C Debug -V

The ``--test-dir`` flag specifies the directory where the build is located. The ``-C`` flag specifies the configuration to use.
The ``-V`` flag indicates that the tests should be run in verbose mode.

If using VSCode or any other IDE, it is also possible to run the tests directly from it. Please refer to the respective software documentation for instructions on how to run the tests with CMake and the IDE.

Clesperanto project relies on a continuous integration system that runs the tests on every commit to ensure the stability of the codebase for multiple platforms (MacOS, Windows, and Ubuntu).
This drastically reduces the chances of bugs being introduced in the codebase and ensures that the library remains functional across different environments.
However, it is still recommended to run the tests locally after building the library to ensure everything is working as expected.

It is also an important step for developers who are contributing to the project. 

.. important::

    Tests in ``Release`` mode will always pass. For a proper test run, you should build in ``Debug`` mode.

.. note::

  If built traditionally, the root directory of the build should be ``./build/{config_type_build}/``, where ``{config_type_build}`` depends on the system and configuration used, e.g., ``./build/linux-ninja-multi/`` for Ubuntu systems.

.. hint::

  It is also possible to run a particular test using the ``ctest`` command: ``ctest --test-dir ./build -C Debug -R {test_name}``.


Troubleshooting
---------------

If you encounter issues during the build or test process that you cannot resolve or consider them bugs, please report them on the `GitHub Issues page <https://github.com/clEsperanto/CLIc/issues>`.
