How to use
==========

.. container:: text-justify

   **Note on Direct Usage:** CLIc is primarily intended as a backend for higher-level libraries like pyclesperanto and clesperantoJ, which provide user-friendly APIs.
   Direct use of CLIc is recommended only when you need to implement new operations or integrate it into your own C++ project.

   If you're looking for a simpler, more accessible interface, consider using one of the higher-level bindings instead.
   This section provides a practical example for developers who do need to work with CLIc directly.

Initialization
~~~~~~~~~~~~~~~

**Step 1: Initialize the Backend**

CLIc uses a singleton pattern (via ``BackendManager``) to manage a single, globally-accessible backend instance. This ensures consistent device and resource management throughout your application.
Initialize it by specifying which compute backend to use:

.. code-block:: c++

    #include "cle.hpp"
    /* ... */
    cle::BackendManager::getInstance().setBackend("opencl");

The ``cle::BackendManager::getInstance()`` function returns the singleton instance of the backend manager.
The ``setBackend("opencl")`` call initializes the OpenCL backend—currently the only backend available—and automatically discovers all compatible devices (GPUs, CPUs, etc.) on your system.
If no compatible devices are found, an error is thrown.

**Step 2: Initialise a Device**

All GPU operations must be executed on a specific device. Before running operations, you need to select which device (GPU or CPU) to use from the backend.
You can retrieve a device using ``getDevice()`` or ``getDeviceByIndex()`` from the backend, specifying the device name/substring and device type filter:

.. code-block:: c++

    auto device = cle::BackendManager::getInstance().getBackend().getDevice("", "all");

This selects the first available device of any type. The empty string matches any device name, and ``"all"`` means any device type (GPU or CPU).

If you have multiple devices with the same name, identify them by index:

.. code-block:: c++

    auto device = cle::BackendManager::getInstance().getBackend().getDeviceByIndex(1, "gpu");


Data transfer
-------------

**Understanding cle::Array**

``cle::Array`` represents an allocated block of memory on a GPU device. Like standard C++ containers, it has constructors and read-only accessors, but setters are intentionally limited to prevent inconsistencies between device memory and the CPU representation.

**Creating an Array**

To create an array on the device, provide the device reference, dimensions, data type, and memory type:

.. code-block:: c++

    auto gpu_array = cle::Array::create(10, 5, 3, 3, cle::dType::FLOAT, cle::mType::BUFFER, device);

This creates a 3D array of size 10x5x3 with ``float`` elements in device memory (similar to ``malloc()`` in C).
The dimensions follow the convention: width, height, depth. The ``cle::mType::BUFFER`` specifies the memory layout type—see the `Array class documentation <https://clesperanto.github.io/CLIc/array.html>`__ for other memory types.

**Writing Data to the Device**

After creating the array, transfer data from your CPU to the device:

.. code-block:: c++

    gpu_array->writeFrom(array.data());

The ``writeFrom()`` method copies data from your CPU array to the device. The source array must be a ``std::vector`` or ``std::array`` with matching size and data type.

**Reading Data from the Device**

To retrieve results from the device back to your CPU:

.. code-block:: c++

    gpu_array->readTo(array.data());

The ``readTo()`` method transfers data from the device back to a CPU ``std::vector`` or ``std::array``.

**Important Notes on Memory Transfers**

.. note::

    Both ``readTo()`` and ``writeFrom()`` are **blocking functions**—they wait for the operation to complete before returning. Consider performance implications for large data transfers.

.. warning::

    CLIc performs minimal validation at this low-level API. The developer is responsible for ensuring:
    
    - Array sizes match (both value and type)
    - Data types are compatible
    - Device memory is sufficient
    
    Mismatches result in undefined behavior. Always verify your array configurations.

Execute an Operation
~~~~~~~~~~~~~~~~~~~~

Once you have data on the device, you can execute GPU operations. Here's an example using the ``add_image_and_scalar`` operation:

.. code-block:: c++

    auto gpu_result = cle::tier1::add_image_and_scalar(device, gpu_array, nullptr, 5);

This operation adds the scalar value 5 to every element in ``gpu_array`` and returns a new array with the results.
The parameters are: the target device, the input array, an optional output array (``nullptr`` creates one automatically), and operation-specific parameters.

**Memory Requirements for Operations**

.. note::

    Most CLIc operations require additional temporary memory on the device during execution:
    
    - Simple operations typically need ~2x the input array size
    - Complex operations may need significantly more space for intermediate calculations
    
    If you encounter memory errors, ensure your device has sufficient free memory or use smaller input arrays.

Execute a mini-pipeline
~~~~~~~~~~~~~~~~~~~~~~~

Combining multiple operations into a processing pipeline is straightforward. `clesperanto` is designed to facilitate chaining operations together efficiently.

.. code-block:: c++

    /* 
     * Prepare input, output containers on CPU and allocate a device 
     */

    auto gpu_input = cle::Array::create(10, 5, 3, 3, cle::dType::FLOAT, cle::mType::BUFFER, device);
    gpu_input->writeFrom(cpu_input.data());

    auto gpu_blurred = cle::tier1::gaussian_blur(device, gpu_input, nullptr, 1.0, 1.0, 1.0);
    auto gpu_thresholded = cle::tier4::threshold_otsu(device, gpu_blurred, nullptr);
    auto gpu_labeled = cle::tier5::connected_components_labeling_box(device, gpu_thresholded, nullptr);

    gpu_labeled->readTo(cpu_output.data());