Core
----

List of core classes from the `net.clesperanto.core` package. These classes handle the main functionalities of clesperantoj and the management of 
The BackendJ and DeviceJ classes are responsible for managing the computational backends (OpenCL, CUDA, etc.) and hardware devices used for processing.

.. doxygenclass:: net::clesperanto::core::BackendJ
	:project: clesperantoj
	:members:

.. doxygenclass:: net::clesperanto::core::DeviceJ
	:project: clesperantoj
	:members:

The ArrayJ is the data structure used to represent images and multidimensional arrays in clesperantoj. The MemoryJ class manages memory allocation, deallocation, and data transfer between the host and device.

.. doxygenclass:: net::clesperanto::core::ArrayJ
	:project: clesperantoj
	:members:

.. doxygenclass:: net::clesperanto::core::MemoryJ
	:project: clesperantoj
	:members:

.. .. doxygenclass:: net::clesperanto::core::Utils
.. 	:project: clesperantoj
.. 	:members:

.. .. doxygenclass:: net::clesperanto::core::DataType
.. 	:project: clesperantoj
.. 	:members:

.. .. doxygenclass:: net::clesperanto::core::MemoryType
.. 	:project: clesperantoj
.. 	:members:
