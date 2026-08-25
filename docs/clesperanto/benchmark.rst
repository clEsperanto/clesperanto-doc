Benchmarking
############

Benchmarking was done with the Python version of clesperanto, as it is the easiest to use and the most commonly used.
We compared the performance of clesperanto, with its different backends, to the performance of the NumPy (CPU) and CuPy (GPU) libraries.
The goal is not to compete, but to evaluate the performance of clesperanto against state-of-the-art libraries and to provide a reference for users choosing the best backend for their needs.

The benchmark was designed based on the benchmarking approach used by CuPy (https://cupy.dev/) and is available `here <https://github.com/clesperanto/clesperanto/tree/main/benchmarks>`__.
It was run on a small (128MB) and a large (2GB) 3D array. Each operation was run multiple times and the average time was taken.

.. container:: figure-centered
    
    .. figure:: ./images/boxplot_128_MiB_128x512x512.png
        :alt: benchmarking results for 128MB 3D array
        :width: 90%

    .. figure:: ./images/boxplot_2.0_GiB_128x2048x2048.png
        :alt: benchmarking results for 2GB 3D array
        :width: 90%


Additional information: 
- CuPy Matrix multiplication rely on the ``cuBLAS`` library, which is highly optimized for NVIDIA GPUs. OpenCL implementations will not be able to compete with this performance (https://cnugteren.github.io/tutorial/pages/page1.html) 
- Slicing operations in CuPy can rely on views, which are very fast. pyclesperanto only supports views for continuous slices.

Operations details
==================

- Simple element-wise operations: Simple addition of an array with a scalar
- Complex element-wise operations: Element-wise mathematical equation between two arrays involving several operators (power, cosine, sine)
- Simple reduction operations: Sum reduction of all elements in an array
- Complex reduction operations: Standard deviation reduction of all elements in an array
- `Convolution operations <https://en.wikipedia.org/wiki/Convolution>`_: Euclidean convolution of an array with a kernel of radius 7
- `Advanced convolution operations <https://en.wikipedia.org/wiki/Convolution>`_: Gaussian separable convolution of an array with sigma 7
- `Matrix multiplication <https://en.wikipedia.org/wiki/Matrix_multiplication>`_: Matrix multiplication of two 2D arrays (only the first ``yx`` slice of the 3D array is used)
- Strided array slicing: Accessing a non-continuous part of an array
- `Fast Fourier Transform <https://en.wikipedia.org/wiki/Fast_Fourier_transform>`_: Applying a FFT on an array


Runners configuration
=====================

The benchmark combines results from different CPU and GPU runners. The following table shows the runners used for the benchmark.
We aim to add more runners in the future as we extend our tests and gain access to more hardware. Do not hesitate to contact us if you have access to some fancy or uncommon hardware and want to contribute to the benchmark.

.. table:: Runner Devices
   :widths: auto
   :align: left

   =======================  ========================================  
   GPUs                     CPUs                                      
   =======================  ========================================  
   Apple M5 Max             Apple M5 Max                              
   NVIDIA GeForce RTX 3090  Intel(R) Xeon(R) Gold 6326 CPU @ 2.90GHz  
   NVIDIA Tesla V100 32GB                                               
   NVIDIA A100 40GB                                               
   =======================  ========================================  





