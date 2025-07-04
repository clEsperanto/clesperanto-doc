Installation
============

From repository (Recommended)
-----------------------------

We are using the `Maven SciJava repository <https://maven.scijava.org/#nexus-search;quick~clesperantoj>`_ to distribute clesperantoj.
To use it in your Maven project, add the following to your ``pom.xml``: 

.. code-block:: xml

    <dependency>
        <groupId>net.clesperanto</groupId>
        <artifactId>clesperantoj</artifactId>
        <version>0.16.9</version>
    </dependency>


From source
-----------

For Development, or if you are using a platform not supported by the package managers, you can build ``clesperantoj`` from source.

To build it, you need to have the following installed on your system:
- a Java Development Kit (JDK) version 8 or later (`zulu <https://www.azul.com/downloads/?package=jdk#zulu>`_, openjdk, oracle, etc.)
- Apache `Maven <https://maven.apache.org/>`_
- `Git <https://git-scm.com/downloads>`__
- `CMake <https://cmake.org/download/>`__ (version 3.20 or higher)
- a C++ Compiler:
    - On Windows, you can install it with `MSVC <https://visualstudio.microsoft.com/>`__
    - On macOS, you can install the `Xcode command line tools <https://developer.apple.com/xcode/resources/>`__
    - On Linux, you can install GCC with the `build-essential <https://packages.ubuntu.com/jammy/build-essential>`__ package.
    - Or any other compiler that supports C++17 should work.

.. important::

   Ensure that all the following software are available in your system's ``$PATH`` variable and accessible from your terminal.
   Please, refer to the respective software documentation for installation instructions and usage.

You can then build the project by cloning the repository with ``git`` and running ``mvn install``.

.. code-block:: bash

    git clone https:://github.com/clEsperanto/clesperantoj_prototype.git
    cd clesperantoj_prototype
    mvn install

Once built, the `jar` file will be available in the ``target`` directory as well as installed in your local Maven repository.

