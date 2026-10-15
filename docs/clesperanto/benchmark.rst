Benchmarking
############

Benchmarking was done with the Python version of clesperanto, as it is the easiest and the most commonly used, with baselines libraries NumPy and CuPy to compare against. 
We compared the performance of the differents backends ``CUDA``, ``OpenCL``, and ``Metal`` to the performance of the ``NumPy`` (CPU) and ``CuPy`` (GPU) libraries.
The goal is not to compete, but to observe and evaluate the performance of clesperanto against state-of-the-art libraries and to provide a reference for users choosing the best backend for their needs.

The benchmark was designed and adapted from the benchmarking approach used by ``CuPy`` (https://cupy.dev/) and is available `here <https://github.com/clesperanto/clesperanto/tree/main/benchmarks>`__.
It was run on a small (128MB) and a large (2GB) 3D array, with a warmup and repeated runs to compute an average time.

.. container:: figure-centered
    
    .. figure:: ./images/boxplot_128_MiB_128x512x512.png
        :alt: benchmarking results for 128MB 3D array
        :width: 90%

    .. figure:: ./images/boxplot_2.0_GiB_128x2048x2048.png
        :alt: benchmarking results for 2GB 3D array
        :width: 90%

.. note::

    - CuPy Matrix multiplication rely on the ``cuBLAS`` library, which is highly optimized. OpenCL implementations will not be able to compete (https://cnugteren.github.io/tutorial/pages/page1.html) 
    - Slicing operations in ``CuPy`` relies on views, avoiding copying of data, which can explain high performance differences.

We can observe some interesting variability in the results of pyclesperanto which seems to be dependent on the OS and the GPU used. 
It is usually advised to the use the pyclesperanto backend corresponding to the GPU vendor (e.g., ``CUDA`` for NVIDIA GPUs, ``Metal`` for Apple GPUs, and ``OpenCL`` for others) with some exceptions to Windows users, where ``OpenCL`` seems to be sometimes more efficient thant is ``CUDA`` counterpart.
Overall, the results show that clesperanto is competitive with state-of-the-art libraries and can provide a valide alternative for users looking for an easy-to-use and efficient GPU computing library for Image Processing that can run on a wide range of systems and hardware.

The Numpy was run on an ``Apple M5 Max`` and an ``Intel(R) Xeon(R) Gold 6326 CPU @ 2.90GHz``.
Pyclesperanto was run on an ``Apple M5 Max``, an ``NVIDIA Quadro RTX 8000``, an ``NVIDIA Tesla V100``, and an ``NVIDIA A100``. 
Cupy was run on the same devices as pyclesperanto, except for the ``Apple M5 Max`` which is not supported.

Operations details
==================

- Simple element-wise operations: Simple addition of an array with a scalar
- Complex element-wise operations: Equation between two arrays involving expensives operators (power, cosine, sine)
- Simple reduction operations: Sum reduction of all elements in an array into a scalar
- Complex reduction operations: Standard deviation reduction of all elements in an array into a scalar
- `Convolution operations <https://en.wikipedia.org/wiki/Convolution>`_: Euclidean convolution of an array with a array kernel of radius 7
- `Advanced convolution operations <https://en.wikipedia.org/wiki/Convolution>`_: Gaussian separable convolution of an array with sigma 7
- `Matrix multiplication <https://en.wikipedia.org/wiki/Matrix_multiplication>`_: Matrix multiplication of two 2D arrays (only the first slice is used)
- Strided array slicing: Accessing a non-continuous part of an array
- `Fast Fourier Transform <https://en.wikipedia.org/wiki/Fast_Fourier_transform>`_: Applying a FFT on an array

