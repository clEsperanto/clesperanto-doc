API documentation
#################

Array Class
===========

The ``Array`` class is the primary data structure class of the library.
It stores the pointer to the memory space in the ``Device``, along with the necessary information to access and manipulate it.
The class is intended to be used through smart pointers defined as ``Array::Pointer`` and should not be accessed directly.
Hence, the creation of an ``Array`` object is done through ``Array::create()`` function.

The class provides a set of methods that describe the array, such as its ``size``, ``width``, ``dtype``, among others.
It also provides methods to write/read data to and from the host, and to perform operations on the array, such as ``fill`` and ``copy``.

This object is the main input and output of the library functions.

.. doxygenclass:: cle::Array
    :members:

Backend Manager
===============

The Backend Manager is a singleton class that manages backend selection and initialization.
It is designed to allow only one backend to be active at a time. Users can select
backends at runtime, during the initialization phase.
By default, the library will try to initialize the OpenCL backend.
If initialization fails, it will attempt to initialize the CUDA backend.
If both fail, the library will throw an exception.

.. warning::

    Switching between backends during runtime is not supported and may lead to undefined behavior.

.. doxygenclass:: cle::BackendManager
    :members:


Backend Class
=============

The `Backend` class is an abstract class defining the interface for the different hardware backends supported by CLIc.
Inherited classes implement the necessary low-level functions to operate the hardware.
This abstraction enforces a design pattern allowing switching between different hardware backends without changing the high-level code.
Currently, the library supports OpenCL and CUDA backends, with the possibility of adding more in the future.

.. note::

    This class operates closest to the hardware, and casual developers should not need to interact with it.

.. warning::

    The `CUDABackend` class is operational but not yet fully released.

.. doxygenclass:: cle::Backend
    :members:

OpenCL Backend
==============

.. doxygenclass:: cle::OpenCLBackend
    :members:

CUDA Backend
============

.. doxygenclass:: cle::CUDABackend
    :members:

Device Class
============

A ``Device`` is a processing unit that can execute OpenCL kernels.
It is mainly a GPU, but it can also be a CPU or a simulation of a device (e.g. `pocl`, `oclgrind`).
It is a good practice to consider a device as a mini computer with its own memory with which you can communicate through the OpenCL API.
This class holds a set of information allowing the identification of a specific hardware for future communication with it during execution.


The class has no processing functions; it is mainly used to store necessary information required to identify the hardware.
The detection and the communication is managed by ``Backend`` class.

Users should not need to interact with the ``Device`` class extensively, except during the initialization of the library or when using multiple devices for computation.

.. doxygenclass:: cle::Device
    :members:


Operation list
==============

The tiers hold the different operations that are available in CLIc.
These operations are grouped by their complexity, following the rules that a function in tier N implement a function from tier N-1.
This organisation is only visible in ``CLIc`` and is not exposed to the user. It is mainly an internal organisation to facilitate the development and the maintenance of the library. 

tier1
-----

.. doxygennamespace:: cle::tier1
    :members:

tier2
-----

.. doxygennamespace:: cle::tier2
    :members:

tier3
-----

.. doxygennamespace:: cle::tier3
    :members:

tier4
-----

.. doxygennamespace:: cle::tier4
    :members:

tier5
-----

.. doxygennamespace:: cle::tier5
    :members:

tier6
-----

.. doxygennamespace:: cle::tier6
    :members:

tier7
-----

.. doxygennamespace:: cle::tier7
    :members:

tier8
-----

.. doxygennamespace:: cle::tier8
    :members:
