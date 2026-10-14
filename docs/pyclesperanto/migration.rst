`prototype` migration
=====================

This guide helps users migrate from `pyclesperanto_prototype <https://github.com/clEsperanto/pyclesperanto_prototype>`_ to the current `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_ version.

This document is not exhaustive and may not cover all changes, even though we tried to cover the most important ones. We appreciate any feedback and contributions to improve this migration guide via GitHub issues, pull requests, or direct messages to the maintainers.

Overview
--------

The transition from ``pyclesperanto_prototype`` to ``pyclesperanto`` represents a significant architectural evolution of the library:

- **Backend Abstraction**: Supports for multiple different backends (OpenCL, CUDA, Metal)
- **Device Management**: Improved device selection and management
- **API Rework**: Renamed or refactored for better consistency

Key Architectural Changes
-------------------------

1. **Import Structure**
   
   Old (pyclesperanto_prototype)::
   
       import pyclesperanto_prototype as cle
       
   New (pyclesperanto)::
   
       import pyclesperanto as cle

2. **Backend Selection**

    pyclesperanto_prototype used OpenCL by default. The new version requires explicit backend installation and selection::
    
        # Install a backend
        pip install pyclesperanto[opencl]   # for OpenCL
        pip install pyclesperanto[cuda]     # for CUDA
        pip install pyclesperanto[metal]    # for Metal
        pip install pyclesperanto[all]      # for all possible backends on your platform
        
        # Select backend at runtime
        import pyclesperanto as cle
        cle.list_available_backends()
        > ['opencl', 'cuda', 'metal']
        cle.select_backend("opencl")  # or "cuda", "metal"

    OpenCL is the default backend that is always available.

3. **Device Management**

    Both versions support device management in a similar way::
    
        cle.list_available_devices()
        > ['Intel(R) UHD Graphics 630', 'NVIDIA GeForce RTX 3090', 'Apple M1 Pro']
        device = cle.get_device() # Return the current selected device
        cle.select_device(device)
        
    The Device object can now be passed to functions for multi-device processing and can also be selected by index.

4. **Array/Image Creation**

   Both versions have similar array creation functions::
   
       # Both support similar patterns
       image = cle.create((100, 100), dtype=float)
       image = cle.zeros((100, 100))
       image = cle.push(numpy_array)

   and array reading functions::
    
       numpy_array = cle.pull(image)
       numpy_array = image.get()
       numpy_array = np.asarray(image)

    ``pyclesperanto.Array`` try to follow the NumPy API as much as possible, with some limitations due to implementation and GPU limitations.


Function API changes
--------------------

Although we try to keep as much as possible the same API, several functions from `pyclesperanto_prototype` have been renamed in `pyclesperanto` for better consistency and clarity.
In a vast majority of cases, we kept a legacy function which should now be tagged as deprecated and with a warning message to redirect you to the function to replace it with. 

In addition, to assist people in the transition, we have created an autoamtic correspondance notes between the two versions, which can be found in the `Transition Notes repository <https://github.com/clEsperanto/pyclesperanto-transition-notes/blob/main/transition_notes.md>`_.

If you still have questions or need assistance with specific functions, or that you notice any discrepancies in the transition notes, please reach out to us via GitHub issues.