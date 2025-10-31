Usage
=====

pyClesperanto is a GPU-accelerated image processing library for Python. To get started, import the library:

.. code:: python

    import pyclesperanto as cle

.. warning::

    If you encounter an error at this stage, the OpenCL driver is likely not installed or your device is not OpenCL-compatible.
    Please check the OpenCL installation and driver compatibility with your system.

Next, you can explore the devices available on your computer using the `list_available_devices()` function or get more detailed information with the `info()` function:

.. code:: python

    # Return the name of all available devices on the computer
    print(cle.list_available_devices())

    # Return the name, index, and information on all the devices
    print(cle.info())


To work on a specific device, you need to select it. By default, pyclesperanto automatically selects the last available device at import time.
You can check the current device with the `get_device()` function and switch devices using the `select_device()` function:

.. code:: python

    # Query the current device
    print(cle.get_device())

    # Select a device by name, substring, or index
    cle.select_device("NVIDIA RTX 4090") # full name
    cle.select_device("TX")              # substring
    cle.select_device(0)                 # device index



Memory transfer
---------------

GPU devices have separate memory from your computer. You must transfer data to the device to process it and transfer results back to read them.
This is known as `copy from host to device` and `copy from device to host`. pyclesperanto provides three functions to manage memory transfer:

- `push` is used to transfer/copy data from the host to the device.
- `pull` is used to transfer/copy data from the device to the host.
- `create` is used to allocate empty space on the device, which will be used, for example, to store a result.

These copy operations are costly in terms of time as they scale with the data size. Therefore, it is good practice to avoid them as much as possible once you are optimizing your code.

Create
~~~~~~

The ``create`` function allocates empty memory on the GPU without transferring data. You only need to specify the image size as a tuple of integers following the numpy convention ``zyx``.

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

.. note::

    pyclesperanto does not support `64-bit` data types (`int64`, `float64`) to ensure compatibility with most GPU devices.
    If 64-bit data are provided, they are automatically cast to 32-bit, which may result in precision loss.

Pull
~~~~

The ``pull`` function transfers data from the GPU back to the host. It will be returned as a numpy array.

.. code:: python

    # Pull gpu_image to the host
    arr = cle.pull(gpu_image)

The data type of the array will be the same as the data type of the image on the GPU.

Free memory
~~~~~~~~~~~

Because memory on the GPU can be limited, it is beneficial to free memory when it is no longer needed. In pyclesperanto, you can free memory similarly to Python using the `del` keyword.

.. code:: python

    # Free the memory of the image on the GPU
    del gpu_image


Apply operations on images
--------------------------

Most pyclesperanto functions are filters or mathematical operations on images. The API uses a consistent convention across all functions:

.. code:: python

    cle.function_name(input, output, arg0, arg1, ...)

The `output` parameter is part of the function signature because GPUs cannot automatically allocate memory; you must provide the output location.
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

While explicit, this code gives you full control over data and memory.
Alternatively, you can let pyclesperanto handle memory operations automatically. This simplifies your code but may not be optimal for all memory usage patterns:

.. code:: python

    # Apply a Gaussian blur directly on a numpy array and save the result in a pyclesperanto array
    gpu_output = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)
    # Pull back the result to the host
    result = cle.pull(gpu_output)

In this approach, ``cpu_image`` is automatically pushed to the GPU and output memory is allocated when ``gaussian_blur`` is called.
The function returns a ``pyclesperanto array``, and memory transfers happen in the background without explicit management.

Pipeline of operations
----------------------

Since most pyclesperanto operations are filters, you can chain them together to create processing pipelines.
For example, to apply a Gaussian blur followed by a threshold:

.. code:: python

    # Apply a Gaussian blur
    gpu_input = cle.push(cpu_image)
    gpu_output = cle.create(cpu_image.shape)
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    blurred = cle.pull(gpu_output)

    # Apply a threshold
    gpu_input = cle.push(blurred)
    gpu_output = cle.create(blurred.shape)
    cle.greater_constant(gpu_output, gpu_output, constant=0.5)
    binarized = cle.pull(gpu_output)

While correct, this approach is inefficient because of intermediate ``push`` and ``pull`` operations. It's useful for prototyping to inspect intermediate results.
For optimized code, chain operations together to minimize memory transfers:

.. code:: python

    # Apply a Gaussian blur
    gpu_blurred = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)
    # Apply a threshold
    gpu_binarized = cle.greater_constant(gpu_blurred, constant=0.5)
    # Read the output on host
    binarized = cle.pull(gpu_binarized)

This approach uses only one ``push`` (inside ``gaussian_blur``) and one ``pull`` at the end of the pipeline.
Output memory is automatically allocated for each operation, minimizing unnecessary data transfers.
