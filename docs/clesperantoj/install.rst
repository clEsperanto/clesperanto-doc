Installation
============

Prerequisites Overview
----------------------

Before installing clesperantoj, ensure you have the required software installed and accessible from your terminal's ``$PATH``.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Software
     - Minimum Version
     - Purpose
   * - Java Development Kit (JDK)
     - 8+
     - Compile and run Java code
   * - Apache Maven
     - 3.6.0+
     - Build and dependency management
   * - Git
     - Latest
     - Clone the repository
   * - CMake
     - 3.20+
     - Build native C++ components
   * - C++ Compiler
     - C++17 compatible
     - Compile native libraries

**Quick Verification**: Open a terminal and run these commands to verify your setup:

.. code-block:: bash

    java -version          # Check JDK installation
    javac -version         # Check Java compiler
    mvn --version          # Check Maven installation
    git --version          # Check Git installation
    cmake --version        # Check CMake installation


From Maven Repository (Recommended)
------------------------------------

The easiest way to use clesperantoj is to add it as a dependency in your Maven project via the `Maven SciJava repository <https://maven.scijava.org/#nexus-search;quick~clesperantoj>`_.

**Step 1: Add the Repository**

If your project doesn't already include the SciJava repository, add it to your ``pom.xml``:

.. code-block:: xml

    <repositories>
        <repository>
            <id>scijava.public</id>
            <url>https://maven.scijava.org/content/groups/public</url>
        </repository>
    </repositories>

**Step 2: Add the Dependency**

Add clesperantoj to your project dependencies in ``pom.xml``:

.. code-block:: xml

    <dependency>
        <groupId>net.clesperanto</groupId>
        <artifactId>clesperantoj</artifactId>
        <version>0.16.9</version>
    </dependency>

**Step 3: Verify Installation**

Run Maven to download dependencies:

.. code-block:: bash

    mvn clean dependency:tree

This will download clesperantoj and display your project's dependency tree.

.. tip::

    To find available versions of clesperantoj, visit the `SciJava Repository Search <https://maven.scijava.org/#nexus-search;quick~clesperantoj>`_.


Building from Source
--------------------

Build from source for development, or if you need to use a platform not yet supported by Maven Central.

**Installing Prerequisites**

Refer to the `Prerequisites Overview`_ section above, then follow the platform-specific instructions below.

**Java Development Kit (JDK)**

- **Windows/macOS/Linux**: Download from `Azul Zulu <https://www.azul.com/downloads/?package=jdk#zulu>`_, `OpenJDK <https://openjdk.java.net/>`_, or `Oracle <https://www.oracle.com/java/>`_
- Recommended: Use JDK 11 or newer (JDK 8 is minimum)
- Verify installation: ``java -version``

**C++ Compiler**

- **Windows**: Install `Microsoft Visual C++ Build Tools <https://visualstudio.microsoft.com/downloads/>`_ or full Visual Studio
- **macOS**: Install Xcode command line tools:

  .. code-block:: bash

      xcode-select --install

- **Linux (Ubuntu/Debian)**: Install build tools:

  .. code-block:: bash

      sudo apt-get update
      sudo apt-get install build-essential cmake

- **Linux (Fedora/RHEL)**: 

  .. code-block:: bash

      sudo dnf groupinstall "Development Tools"
      sudo dnf install cmake

**Apache Maven**

Download from `Maven's official website <https://maven.apache.org/download.cgi>`_ and follow `installation instructions <https://maven.apache.org/install.html>`_.

**Build Steps**

Clone the repository and build:

.. code-block:: bash

    git clone https://github.com/clEsperanto/clesperantoj_prototype.git
    cd clesperantoj_prototype
    mvn clean install

.. note::

   The build process compiles both Java code and native C++ components. This may take 5-15 minutes depending on your system.

**Verify the Build**

After successful compilation, you should see:

.. code-block:: bash

    [INFO] BUILD SUCCESS

The compiled artifacts will be available in two locations:

1. **Local directory**: ``target/`` folder (contains JAR file and native libraries)
2. **Local Maven repository**: ``~/.m2/repository/net/clesperanto/clesperantoj/`` (installed for other projects to use)

**Building and Running Tests**

To run the test suite:

.. code-block:: bash

    mvn test

To build without running tests:

.. code-block:: bash

    mvn clean install -DskipTests

.. important::

   Ensure that all required software is available in your system's ``$PATH`` variable and accessible from your terminal.
   Please refer to the respective software documentation for detailed installation instructions.


Troubleshooting
---------------

**Maven command not found**
    Ensure Maven's ``bin`` directory is in your ``$PATH``. Verify with ``mvn --version``.

**CMake version too old**
    Update CMake to version 3.20 or newer. Download from `cmake.org <https://cmake.org/download/>`_.

**C++ compiler not found during build**
    On Linux, ensure you have the development tools installed (see `C++ Compiler`_ section above).
    On Windows, ensure Visual Studio Build Tools are properly installed.

**Native compilation errors**
    These typically occur on unsupported platforms or with missing compiler dependencies.
    Check your C++ compiler version supports C++17: ``g++ --version`` (Linux/macOS).

**Dependency conflicts in Maven**
    Clear your local Maven cache and rebuild:

    .. code-block:: bash

        rm -rf ~/.m2/repository/net/clesperanto
        mvn clean install

**Cannot find SciJava repository**
    Check your internet connection. If behind a proxy, configure Maven in ``~/.m2/settings.xml``.
    For more help, see `Maven Proxy Configuration <https://maven.apache.org/guides/mini/guide-proxies.html>`_.

.. important::

   Ensure that all required software is available in your system's ``$PATH`` variable and accessible from your terminal.
   Please refer to the respective software documentation for detailed installation instructions.

