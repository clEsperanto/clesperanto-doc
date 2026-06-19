Overview
########

.. container:: text-justify

    clesperanto is a multi-language and multi-platform framework for GPU-accelerated image processing.
    It aims to remove language barriers in the scientific image analysis community by providing GPU-accelerated algorithms and a unified API interface across different programming languages and frameworks.

    The project is organized into a set of core-repository APIs, each dedicated to a programming language, and a set of plugins or assistants targeting the main BioImage Analysis frameworks (Fiji, Napari, etc.).
    Each API exposes the same set of GPU-accelerated image processing functions and shares the same underlying C++ codebase.

    The project relies on `OpenCL <https://www.khronos.org/opencl/>`_ to ensure compatibility with a wide range of GPU hardware from different vendors (NVIDIA, AMD, Intel, etc.) and different device types (dedicated graphics cards, integrated GPUs, and even some CPUs).
    It also provides additional support for other frameworks such as `CUDA <https://developer.nvidia.com/cuda-zone>`_ and `Metal <https://developer.apple.com/metal/>`_ to allow direct integration with other libraries and maximize adaptability to different environments.

The core-repository APIs consist of the following repositories:

- |:rocket:| `CLIc <https://github.com/clEsperanto/CLIc>`_ C++ API & project backend
- |:coffee:| `clesperantoJ <https://github.com/clEsperanto/clesperantoj_prototype>`_ Java API
- |:snake:| `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_ Python API

