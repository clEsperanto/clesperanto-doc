Converters
----------

clesperantoj provides various converters to transfer data between different scientific java libraries for image processing.
These converters facilitate interoperability and make it easier to integrate different libraries into a single workflow.
Each converter ships two methods: one for converting from the target library to clesperantoj, and one for converting from clesperantoj to the target library.
These are equivalent to the `push` and `pull` concepts.

.. doxygennamespace:: net::clesperanto::imglib2
	:project: clesperantoj
	:members:
	:content-only:


.. doxygennamespace:: net::clesperanto::imagej
	:project: clesperantoj
	:members:
	:content-only: