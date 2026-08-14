`prototype` migration guide
===========================

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
        cle.select_backend("opencl")  # or "cuda", "metal"

    OpenCL is the default backend if no selection is made.

3. **Device Management**

    Both versions support device management in a similar way::
    
        device = cle.get_device()
        cle.select_device(device)
        
    The Device object can now be passed to functions for multi-device processing.

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

Function API changes
--------------------

For consistency and clarity, several functions from `pyclesperanto_prototype` have been renamed or consolidated in `pyclesperanto`.
This comes with either parameter renames, function aliases, or complete removal of certain functions.

To help you navigate these changes as you migrate your code, we have created a comprehensive list of function changes:

- `https://github.com/clEsperanto/pyclesperanto-transition-notes/blob/main/transition_notes.md`_.

If you still have questions or need assistance with specific functions, or that you notice any discrepancies in the transition notes, please reach out to us via GitHub issues.