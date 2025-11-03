Contributing to pyclesperanto: the Python Wrapper
=================================================


Experimental subpackage
-----------------------

pyclesperanto is shipped with an `experimental` subpackage that is dedicated to the development of new image processing functions and kernels.
This subpackage is empty by default, except for a demo implementation of the CLAHE algorithm, and is dedicated to contributions and experimental filters.
We accept OpenCL kernels contribution as well as higher-level Python functions that combine existing kernels into more complex processing pipelines.

New core functionality
----------------------

pyclesperanto relies on a C++ backend library (CLIc) that implements the GPU ressources management and the established image processing kernels.






Fork and PRs
------------

Contributions are welcome under PRs (Pull Requests) to the main repository.
Ideally the PR should be detailed on what it does and why it is needed.

Experimental subpackage
-----------------------

For new kernel or processing function, we recommend you use the `experimental` subpackage of pyclesperanto.
This subpackage is dedicated for the development of additional functions without having to modify the core library or risk breaking existing functionality.
It can also provide a space for beta testing new features before they are moved to the main package.

By default, this subpackage is empty with the exception of the `clahe` kernel that we kept for demonstration purposes.
We advise you to also look at `how to run custom OpenCL kernels <https://github.com/clEsperanto/pyclesperanto/blob/main/demos/api/execute_custom_opencl_kernel.ipynb>`_ in the tutorials and demos.

And we will happily accompany you in the process of your contribution, providing guidance and support as needed.

