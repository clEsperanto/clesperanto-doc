Why use clEsperanto?
====================

GPU programming
---------------

GPUs are processors designed to perform parallel computations mainly for graphics rendering, but nowadays they are also used for general-purpose computation, especially in the fields of scientific computing and Artificial Intelligence. 
They are composed of a large number of cores, which individually are not as powerful as a CPU core, but when used in parallel, can perform a large number of small tasks simultaneously. 
In this context, they become relevant for image processing, where many operations can be performed in parallel on pixels or voxels. 

The main difficulty with GPUs is the high technical threshold and effort required to perform operations with them.
To run a calculation on a GPU, you need to develop a kernel — a specific program that performs the calculation on the GPU side — and another program on the CPU side to manage resource allocation and management.
Both the kernel and the program to execute it are based on *C/C++* and framework languages (like *OpenCL*, *CUDA*, etc.), each with its own specificities and constraints.

Several libraries offer wrappers around these GPU programming languages, such as *pyopencl* or *cupy* for Python, which simplify the management side of GPU programming, but leave kernel development to the user.

Hence, even though they are powerful hardware available in most systems and can improve performance on a large variety of tasks, their usage is often limited to experts in the field.

Hardware and Backends
---------------------

GPUs require a specific framework to run, such as *Metal* or *CUDA*, which are directly tied to their manufacturers. 
This means that you cannot use any type of framework with any type of GPU.
*CUDA* is a perfect example, as it can only be used with NVIDIA devices; similarly, *Metal* is its equivalent for Apple devices.
*OpenCL* is an exception, as it is an open standard designed to be used on most hardware, with a few exceptions, but at a certain cost of performance compared to dedicated frameworks when doing heavy computations.
Other frameworks exist, such as *Vulkan* or *HIP*, but they are less commonly used or dedicated to specific use cases like graphics rendering.

Each of these frameworks has its own set of APIs and tools, and will require some specificity in the kernels to be able to run.


Image Processing
----------------

Image processing, being mostly based on element-wise operations on pixels or local neighborhoods of pixels and having a majority of algorithms with complexity directly dependent on the data size, is one of the fields that can benefit from GPU acceleration. 
However, depending on the operation to perform, the number of kernels to develop can be high and complex, an additional difficulty for the user.

It is important to note that not all algorithms are suited for GPU acceleration; for example, algorithms that require recursive operations or that require the entire data in memory at once are not suitable.
Outside of these exceptions, image processing operations like filtering, histogram computation, morphological operations, or image transformation are well suited for GPU acceleration.


Image Processing with clEsperanto
---------------------------------

This is where clEsperanto comes in. 
The library provides an interface to the GPU that simplifies resource management and interaction with the hardware and provides a set of pre-implemented kernels for a large number of image processing operations as well as more generic array operations.
Altogether, it is a fully equipped library to perform image processing on the GPU, with a simple and explicit API for all users, from beginners to experts.
It is particularly well-suited for a full image processing pipeline or as a pre/post-processing step when using deep learning solutions.

To ensure maximum compatibility with all types of hardware, clEsperanto is initially designed to be used with *OpenCL*. 

Efforts could be made in the future to support other frameworks such as *CUDA* and *Metal*, mainly to allow direct links with other libraries that rely on these frameworks, such as *cupy* or *torch*.
