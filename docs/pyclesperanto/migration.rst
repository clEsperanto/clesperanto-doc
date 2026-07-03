`prototype` migration guide
===========================

This guide helps users migrate from `pyclesperanto_prototype <https://github.com/clEsperanto/pyclesperanto_prototype>`_ to the current `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_ version.

This document is not exhaustive and may not cover all changes, even though we tried to cover the most important ones. We appreciate any feedback and contributions to improve this migration guide via GitHub issues, pull requests, or direct messages to the maintainers.

Overview
--------

The transition from ``pyclesperanto_prototype`` to ``pyclesperanto`` represents a significant architectural evolution of the library:

- **Backend Abstraction**: The new version supports multiple backends (OpenCL, CUDA, Metal) with a unified API
- **Modular Structure**: Functions are organized in a cleaner tier-based hierarchy
- **Device Management**: Improved device selection and management
- **API Improvements**: Many functions have been renamed or refactored for better consistency

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

Functions Removed or Renamed
----------------------------

For consistency and clarity, several functions from pyclesperanto_prototype have been renamed or consolidated in pyclesperanto.
This comes with either parameter renames, function aliases, or complete removal of certain functions.

For removal or renaming of functions, pyclesperanto provides a deprecated version of the function which should point to the new function to use instead.
For parameter renames, pyclesperanto does not provide deprecation or overloading, so users should update their code accordingly.

The following functions from pyclesperanto_prototype have been deprecated and renamed in pyclesperanto:

**Array/Buffer Creation Functions**

- ``create_2d_xy``, ``create_2d_xz``, ``create_2d_yx``, ``create_2d_yz``, ``create_2d_zx``, ``create_2d_zy`` → Use ``create()`` with appropriate shape
- ``empty_image``, ``empty_image_like`` → Use ``empty()``, ``empty_like()``, ``zeros()``, ``zeros_like()`` or ``ones()``, ``ones_like()`` instead
- ``create_binary_like``, ``create_labels_like``, ``create_like``, ``create_same_type_like``, ``create_none``, ``create_zyx``, ``create_image`` → Use ``create()``, ``zeros()``, or ``ones()`` and other derived functions with appropriate parameters
- ``push_zyx``, ``pull_zyx`` → Use ``push()`` and ``pull()``, rotation/transpose can be perfomed before or after.

**Operations**

- ``cle_to_numpy`` → Use ``pull()`` or ``np.asarray()`` instead
- ``dilate_box/sphere`` → Renamed ``dilate`` with parameter ``connectivity='box/sphere'```  
- ``erode_box/sphere`` → Renamed ``erode`` with parameter ``connectivity='box/sphere'```  
- ``laplace_box/diamond`` → Renamed ``laplace`` with parameter ``connectivity='box/sphere'```  
- ``maximum_box/sphere`` → Renamed ``maximum_filter`` with parameter ``connectivity='box/sphere'```   
- ``minimum_box/sphere`` → Renamed ``minimum_filter`` with parameter ``connectivity='box/sphere'```  
- ``mean_box/sphere`` → Renamed ``mean_filter`` with parameter ``connectivity='box/sphere'```  
- ``median_box/sphere`` → Renamed ``median`` with parameter ``connectivity='box/sphere'```  
- ``mode_box/sphere`` → Renamed ``mode`` with parameter ``connectivity='box/sphere'```  
- ``nonzero_maximum_box/diamond`` → Renamed ``nonzero_maximum`` with parameter ``connectivity='box/sphere'```  
- ``nonzero_minimum_box/diamond`` → Renamed ``nonzero_minimum`` with parameter ``connectivity='box/sphere'```  
- ``onlyzero_overwrite_maximum_box/diamond`` → Renamed ``onlyzero_overwrite_maximum`` with parameter ``connectivity='box/sphere'```  
- ``variance_box/sphere`` → Renamed ``variance`` with parameter ``connectivity='box/sphere'```  
- ``bottom_hat_box/sphere`` → Renamed ``bottom_hat`` with parameter ``connectivity='box/sphere'```  
- ``closing_box/sphere`` → Renamed ``closing`` with parameter ``connectivity='box/sphere'```  
- ``opening_box/sphere`` → Renamed ``opening`` with parameter ``connectivity='box/sphere'```  
- ``top_hat_box/sphere`` → Renamed ``top_hat`` with parameter ``connectivity='box/sphere'```  
- ``detect_maxima_box`` → Renamed ``detect_maxima`` with parameter ``connectivity='box/sphere'```  
- ``detect_minima_box`` → Renamed ``detect_minima`` with parameter ``connectivity='box/sphere'```  
- ``standard_deviation_box/sphere`` → Renamed ``standard_deviation`` with parameter ``connectivity='box/sphere'```  
- ``average_distance_touching_neighbors`` → Renamed ``mean_distance_touching_neighbors``
- ``average_distance_of_n_nearest_distances`` → Renamed ``mean_distance_n_nearest_neighbors``
- ``average_distance_of_n_far_off_distances`` → Renamed ``mean_distance_n_farthest_neighbors``
- ``generate_touch_portion_within_range_neighbors_matrix`` → Renamed ``generate_partial_touching_area_matrix_within_range``
- ``replace_intensity`` → Renamed ``replace_value``
- ``replace_intensities`` → Renamed ``replace_values``
- ``generate_touch_count_matrix`` → Renamed ``generate_touch_matrix``
- ``read_intensities_from_map`` → Renamed ``read_map_values``
- ``statistics_of_labelled_pixels`` and ``statistics_of_background_and_labelled_pixels`` → Renamed ``labels_statistics`` with parameter ``include_background=True/False``
- ``statistics_of_labelled_neighbors`` → Renamed ``statistics_of_neighbor_labels`` with parameter ``include_background=True/False``
- ``exclude_labels_with_map_values_out_of_range`` → Renamed ``remove_labels_with_map_values_out_of_range``
- ``exclude_labels_with_map_values_within_range`` → Renamed ``remove_labels_with_map_values_within_range``
- ``generate_touch_portion_matrix`` → Renamed ``generate_partial_touching_area_matrix``
- ``standard_deviation_touch_portion`` → Renamed ``standard_deviation_partial_touching_area_matrix``
- ``label_mean_intensity_map`` → Renamed ``mean_intensity_map``
- ``label_pixel_count_map`` → Renamed ``pixel_count_map``
- ``connected_components_labeling`` → Renamed ``connected_component_labeling``
- ``connected_components_labeling_box`` and ``connected_components_labeling_diamond`` → Renamed ``connected_component_labeling`` with parameter ``connectivity='box/sphere'``
- ``combine_horizontally`` and ``combine_vertically`` → Renamed ``concatenate_along_x`` and ``concatenate_along_y``
- ``concatenate_stacks`` → Renamed ``concatenate_along_z`` to match ``concatenate_along_x`` and ``concatenate_along_y``

**Utility Functions**

- ``set_wait_for_kernel_finish`` → Renamed ``wait_for_kernel_to_finish``
- ``cl_info`` → Renamed ``info``
- ``available_device_names`` → Renamed ``list_available_devices``
- ``draw_box``, ``draw_line``, ``draw_sphere`` → Not implemented;
- ``imread`` → Not implemented;
- ``imshow`` → Prefer ``matplotlib`` or ``napari`` for proper visualization. Will mostlikely be deprecated in future.

New Functions in pyclesperanto
------------------------------

The current pyclesperanto version includes many new functions not present in pyclesperanto_prototype.
These provide additional functionality and improved consistency:

- ``acos``, ``asin``, ``atan`` - Inverse trigonometric functions
- ``sin``, ``cos``, ``tan`` - Trigonometric functions
- ``sinh``, ``cosh``, ``tanh`` - Hyperbolic functions
- ``ceil``, ``floor``, ``round``, ``truncate`` - Rounding operations
- ``exponential10``, ``exponential2`` - Base-10 and base-2 exponentials
- ``logarithm10``, ``logarithm2`` - Base-10 and base-2 logarithms
- ``normalize`` - Intensity normalization
- ``binary_closing``, ``binary_opening``, ``binary_dilate``, ``binary_erode`` - Binary morphology with a regular shape footprint
- ``grayscale_closing``, ``grayscale_opening``, ``grayscale_dilate``, ``grayscale_erode`` - Grayscale morphology with a regular shape footprint
- ``binary_infsup``, ``binary_supinf`` - Morphological operations
- ``clahe`` - Contrast Limited Adaptive Histogram Equalization
- ``convolve_fft``, ``deconvolve_fft``, ``fft``, ``ifft`` - Fourier-based operations
- ``gaussian_derivative`` - Derivative of Gaussian filter
- ``hessian_gaussian_eigenvalues`` - Hessian matrix eigenvalues
- ``morphological_chan_vese`` - Active contour segmentation
- ``tubeness`` - Scale-specific Tubeness filter
- ``sato_filter`` - Multiscale tubeness filter
- ``std_x_projection``, ``std_y_projection``, ``std_z_projection`` - Standard deviation projections
- ``parametric_map`` - Generic parametric mapping function that takes a label map and a property map generated from ``labels_statistics()``, along with a property name to map.
- ``pad``, ``unpad`` - Array padding, used for ``fft`` based operations
- ``threshold_mean``, ``threshold_yen`` - Additional thresholding methods, similar to ``threshold_otsu``
- ``percentile`` - Percentile computation

It also introduce the ``evaluate`` function, which allows to combine multiple element-wise operations in a single mathematical expression, improving performance by reducing kernel launches.
This is particularly useful for arythmetic operations. See the documentation for more details on how to use ``evaluate()``.

Resources
---------

- `pyclesperanto GitHub Repository <https://github.com/clEsperanto/pyclesperanto>`_
- `pyclesperanto Documentation <https://clesperanto-doc.readthedocs.io/>`_

For additional help with specific functions, refer to the latest pyclesperanto documentation and API reference.
