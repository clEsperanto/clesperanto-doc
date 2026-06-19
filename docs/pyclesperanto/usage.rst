How to use
==========

pyClesperanto is a GPU-accelerated image processing library for Python. To get started, import the library:

.. code:: python

    import pyclesperanto as cle

.. warning::

    If you encounter an error at this stage, the OpenCL driver is likely not installed or your device is not OpenCL-compatible.
    Please check the OpenCL installation and driver compatibility with your system, or install a different backend (e.g., CUDA) if your device supports it. See :doc:`installation instructions <install>` for more details.


Backends and devices
--------------------

By default, ``pyclesperanto`` uses ``OpenCL`` as a backend, which is automatically selected at import time along with the first available device on your system.
If you installed other backends (e.g., ``CUDA``), you can switch to them with the ``select_backend()`` function:

.. code:: python

    # Select the CUDA backend
    cle.select_backend("CUDA")

.. warning::

    Switching backends will break all existing GPU arrays and operations done with the previous backend. 
    This command should be used only at the beginning of your code before any operation is performed otherwise you may encounter unexpected errors or behavior.

Once a backend is selected, you can query the available devices with ``cle.list_available_devices()`` or get a more detailed list of your devices with ``cle.info()``. 

.. code:: python

    # Return the name of all available devices on the computer
    print(cle.list_available_devices())

    # Return the name, index, and information on all the available devices
    print(cle.info())

.. note::
    
    You may not see the same devices between backends. For example, ``CUDA`` will only show NVIDIA GPUs, while ``OpenCL`` may show both NVIDIA and AMD GPUs, as well as CPUs.

To work on a specific device, you need to select it.
By default, ``pyclesperanto`` automatically selects the first available device at import time, but device order in a system is not guaranteed, and the selected device may not be the one you want to use.

You can check the current selected device with the ``get_device()`` function and switch devices using the ``select_device()`` function:

.. code:: python

    # Query the current device
    print(cle.get_device())

    # Select a device by name, substring, or index
    cle.select_device("NVIDIA RTX 4090") # full name
    cle.select_device("TX")              # substring
    cle.select_device(0)                 # device index


Data transfer
-------------

.. container:: text-justify

    GPU devices have separate memory from your computer. You must transfer data to the device to process it and transfer results back to read them.
    This is known as ``copy from host to device`` and ``copy from device to host``. ``pyclesperanto`` provides three functions to manage memory transfer:

    - ``push`` is used to transfer/copy data from the host to the device.
    - ``pull`` is used to transfer/copy data from the device to the host.
    - ``create`` is used to allocate empty space on the device, which will be used (for example) to store a result.

    These copy operations are costly in terms of time as they scale with the data size. Therefore, it is good practice to avoid them as much as possible when you are optimizing your code.

.. important::

    ``pyclesperanto`` does not support ``64-bit`` data types (``int64``, ``float64``) to ensure compatibility with most GPU devices.
    If 64-bit data is provided, it is automatically cast to 32-bit, which may result in precision loss.

Create
~~~~~~

The ``create`` function allocates empty memory on the GPU without transferring data. You only need to specify the image size as a tuple of integers following the NumPy convention ``(z, y, x)``.

.. code:: python

    # Create an empty image on the GPU of size 100x100
    gpu_image = cle.create((100, 100))

By default, this creates a 32-bit float array. To use a different data type, pass a ``dtype`` argument:

.. code:: python

    # Create an empty image on the GPU of size 100x100 with uint8 data type
    gpu_image = cle.create((100, 100), dtype=np.uint8)

You can also use an existing image as a template, which copies its size and data type:

.. code:: python

    # Create an empty image on the GPU with the same size and data type as the template image
    gpu_image = cle.create_like(template_image)

Push
~~~~

The ``push`` function allocates GPU memory and transfers a data array from your computer to the device.
It expects a numpy array or compatible array-like object (e.g., dask array).

.. code:: python

    arr = np.random.random((100, 100)).astype(np.float32)
    
    # Push arr to the GPU
    gpu_image = cle.push(arr)

The pushed data retains the array's data type. For example, pushing a ``uint8`` array stores it as ``uint8`` on the GPU, using 4 times less memory than a ``float32`` array.
Choosing appropriate data types is important for efficient memory usage on GPUs.

Pull
~~~~

The ``pull`` function transfers data from the GPU back to the host. It will be returned as a numpy array.

.. code:: python

    # Pull gpu_image to the host
    arr = cle.pull(gpu_image)

The data type of the array will be the same as the data type of the image on the GPU.

Free memory
~~~~~~~~~~~

Because memory on the GPU can be limited, it is beneficial to free memory when it is no longer needed. In `pyclesperanto`, you can free memory similarly to Python using the `del` keyword.
By default, memory is automatically freed when a GPU array goes out of scope, but you can also explicitly free memory when you know it is no longer needed to avoid memory overflow or to free up memory for other operations in the same scope.

.. code:: python

    # Free the memory of the image on the GPU
    del gpu_image

Apply operations
----------------

Most ``pyclesperanto`` functions are filters or mathematical operations on images. The API uses a consistent convention across all functions:

.. code:: python

    cle.function_name(input, output, arg0, arg1, ...)

The ``output`` parameter is part of the function signature because GPUs cannot automatically allocate memory; you must provide the output location.
For example, to apply a Gaussian blur:

.. code:: python

    # Push an image to the GPU
    gpu_input = cle.push(cpu_image)

    # Create an output of the same size as the input
    gpu_output = cle.create(cpu_image.shape)

    # Apply a Gaussian blur with sigma_x=2 and sigma_y=2
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)

    # Pull back the result to the host memory
    result = cle.pull(gpu_output)

While explicit and verbose, this code gives you full control over data and memory.
Alternatively, you can let ``pyclesperanto`` handle most memory operations automatically. This simplifies your code but may not be optimal for all memory usage patterns:

.. code:: python

    # Apply a Gaussian blur directly on a numpy array and save the result in a pyclesperanto array
    gpu_output = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)

    # Pull back the result to the host
    result = cle.pull(gpu_output)

In this approach, ``cpu_image`` is automatically pushed to the GPU and output memory is allocated when ``gaussian_blur`` is called.
The function returns a ``pyclesperanto`` array, and memory transfers happen in the background without explicit management.

Pipeline of operations
----------------------

Since most ``pyclesperanto`` operations are filters with inputs and outputs, you can chain them together to create processing pipelines.
For example, to apply a Gaussian blur followed by a threshold:

.. code:: python

    # Push an image to the GPU
    gpu_image = cle.push(cpu_image)

    # Apply a Gaussian blur
    gpu_blurred = cle.gaussian_blur(gpu_image, sigma_x=2, sigma_y=2)

    # Apply a threshold
    gpu_binarized = cle.greater_constant(gpu_blurred, constant=0.5)

    # Read the output on host
    binarized = cle.pull(gpu_binarized)

We can use the output of one operation as the input of the next, chaining the operations together.
Data transfer functions like ``push`` and ``pull`` are only necessary at the beginning and end of the pipeline, once we finish working on the GPU. 

.. note::

    Memory transfer is one of the most costly operations in terms of time. It is good practice to minimize them by keeping data on the GPU as long as possible and only transferring it back to the host when necessary.

Element-wise arithmetic optimization
------------------------------------

``pyclesperanto`` provides arithmetic operations like addition, subtraction, multiplication, and division between arrays in a simple way:

.. code:: python

    # Element-wise arithmetic operations between arrays
    output = (gpu_arr - gpu_arr.min()) / (gpu_arr.max() - gpu_arr.min())

While convenient, this approach is inefficient as it will trigger multiple GPU kernels, leading to lower performance.
When applying multiple arithmetic operations in a row, it is better to chain them together to minimize the number of GPU kernels and memory transfers using the ``evaluate()`` function:

.. code:: python

    # Evaluate an element-wise expression on the GPU as a single kernel
    output = cle.evaluate("(a - a_min) / (a_max - a_min)", {"a": gpu_arr, "a_min": gpu_arr.min(), "a_max": gpu_arr.max()})

In the above example, the expression is evaluated as a single GPU kernel instead of three separate kernels from the first approach.
In addition to arithmetic operators (``+``, ``-``, ``*``, ``/``), the ``evaluate()`` function also supports mathematical functions like ``sqrt()``, ``exp()``, ``log()``, etc.

.. important::

    The ``evaluate()`` function only supports element-wise operations.
    ``gpu_arr.min()`` and ``gpu_arr.max()`` are not element-wise operations but reduction operations; this is why they cannot be included in the expression passed to ``evaluate()``.
    In the example above, ``gpu_arr.min()`` and ``gpu_arr.max()`` are computed separately and passed as arguments to the ``evaluate()`` function.


Interoperability
----------------

Python has a rich ecosystem of libraries for image processing, machine learning, and data analysis, each with its own strengths and weaknesses.
Making them work together can be challenging. In this regard, most libraries follow NumPy ecosystem standards to ensure compatibility and interoperability.
This is also the case for ``pyclesperanto``, which aims to provide seamless interoperability with other libraries when possible.

Working with other CPU libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``pyclesperanto`` is designed to work on GPU devices, so interoperability with CPU-only libraries cannot be copy-free.
A memory transfer from the GPU to the host (or the reverse) is required to exchange data between ``pyclesperanto`` and CPU libraries.

As NumPy is the de-facto standard for array manipulation in Python on CPU, ``pyclesperanto`` provides seamless interoperability with NumPy-like arrays if they provide the ``__array__`` method, which is the case for most array-like objects (e.g., Dask arrays).

.. code:: python

    import torch
    import numpy as np
    import pyclesperanto as cle

    tensor = torch.rand((100, 100))

    # From a PyTorch tensor to a pyclesperanto array through numpy
    gpu_image = cle.asarray(np.asarray(tensor))

    # From a pyclesperanto array to a PyTorch tensor through numpy
    new_tensor = torch.from_numpy(np.asarray(gpu_image))

A more complete demo on how to work with Dask arrays and ``pyclesperanto`` is available in the :doc:`examples and tutorials <examples>` page.

.. note::

    As this interoperability is not copy-free, it will trigger a memory transfer from the device to the host or the reverse, which can be costly in terms of time.

.. note::

    ``cle.asarray()`` is equivalent to ``cle.push()`` and ``np.asarray()`` on a ``pyclesperanto`` array is equivalent to ``cle.pull()``.


Working with other GPU libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other libraries may also support GPU acceleration, and the question of interoperability between GPU libraries becomes more complex.
By default, it is always possible to exchange data between GPU libraries through host memory, similarly to CPU libraries as described in the previous section, but this is not optimal as it involves costly memory transfers.
In specific cases, it is possible to exchange data without memory transfer, which is known as copy-free interoperability.

In ``pyclesperanto``, copy-free interoperability is possible with other libraries supporting the `DLPack protocol <https://dmlc.github.io/dlpack/latest/index.html>`_ and using the same GPU backend language (e.g., ``CUDA``).
An example of copy-free interoperability between ``pyclesperanto`` and ``CuPy`` is shown below.

.. code:: python

    import cupy as cp
    import pyclesperanto as cle

    cle.select_backend("CUDA")

    # Convert a Cupy Array to pyclesperanto Array without memory transfer
    gpu_image_cupy = cp.random.random((100, 100), dtype=cp.float32)
    gpu_image_cle = cle.from_dlpack(gpu_image_cupy)
    
    # Apply image processing operations with pyclesperanto
    gpu_blurred = cle.gaussian_blur(gpu_image_cle, sigma_x=3, sigma_y=3)
    gpu_binary = cle.threshold_otsu(gpu_blurred)
    gpu_labeled = cle.label(gpu_binary)
    
    # Convert the result back to a CuPy array without memory transfer
    gpu_binary_cupy = cp.from_dlpack(gpu_labeled)

.. warning::

    Copy-free conversion between libraries means that data is shared between libraries without memory transfer.
    This can lead to unexpected side effects (for example, when applying in-place operations or if one holder is deleted but not the other).


Tutorials and Examples
----------------------

Several tutorials and examples are available to help you get started with ``pyclesperanto`` and explore its capabilities.
For a complete list of examples and tutorials, please visit the :doc:`examples and tutorials <examples>` page.