benchmarking
############

.. container:: text-justify

    The benchmarking of clesperanto is performed using the `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_ library.
    The choice of the Python API for benchmarking is due to its popularity, ease of use in the scientific community, and it is the most "slow" of the three APIs, which makes it a good candidate for performance testing.
    In addition, the Python ecosystem has other libraries with GPU-acceleration which we can compare against, mainly `cupy <https://cupy.dev/>`_ for NVIDIA GPUs, and `scikit-image <https://scikit-image.org/>`_ for CPU-based image processing.
    Both providing valuable comparisons for the performances.  

    The benchmarking code can be found at this github repository: `benchmark_GPU_python <https://github.com/StRigaud/benchmark_GPU_python>`_.  

    There is a lot of way to benchmark and compare the performance of different libraries, and we will focus on a few specific operation that are key in array and image processing:

    - simple element-wise operations (simple addition with a scalar)
    - complex element-wise operations (element-wise mathematical equation implying several operators and multiple inputs) 
    - simple reduction operations (sum of all elements)
    - complex reduction operations (standard deviation of all elements)
    - `convolution operations <https://en.wikipedia.org/wiki/Convolution>`_ (straightforward convolution with an average size kernel)
    - `advanced convolution operations <https://en.wikipedia.org/wiki/Convolution>`_ (gaussian separable convolution)
    - `matrix multiplication <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ (matrix product of two 2D arrays)
    - non-continous array slicing (accessing a non-continuous part of an array)
    - `Fast Fourier Transform <https://en.wikipedia.org/wiki/Fast_Fourier_transform>`_ (applying a FFT on an array)

    These operations are representative of the most common operations in image processing and array manipulation, and they allow us to evaluate global performance of the libraries in a variety of scenarios, and identify the strengths and weaknesses of each library in different contexts.






