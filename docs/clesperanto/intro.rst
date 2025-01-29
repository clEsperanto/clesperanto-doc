Introduction
============

The clesperanto project is a multi-language and multi-platform framework for GPU-accelerated image processing.
It aims in removing language barriers in the scientific image analysis community by proposing a unified interface API for different programming languages and Frameworks, which rely on a common backend library accelerated by GPU.

The project is organised in a set of core-reposiroty API dedicated each dedicated to a programing language, and a set of plugin or assistant targeting the main BioImage Analysis frameworks (Fiji, Napari, etc.).

The core-repository APIs are composed of the following repositories:

.. .. list-table::
..    :header-rows: 1
..    :widths: 50 50 100

..    * - language
..      - Repository
..      - Descriptions
..    * - |:rocket:|
..      - `CLIc <https://github.com/clEsperanto/CLIc>`_
..      - C++ API & project backend
..    * - |:snake:|
..      - `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_
..      - Python API
..    * - |:coffee:|
..      - `clesperantoJ <https://github.com/clEsperanto/clesperantoj_prototype>`_
..      - Java API

- |:rocket:| : `CLIc <https://github.com/clEsperanto/CLIc>`_ C++ API & project backend
- |:snake:| : `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_ Python API
- |:coffee:| : `clesperantoJ <https://github.com/clEsperanto/clesperantoj_prototype>`_ Java API

and a set of satelite repositories which embeded the core API into the main BioImage Analysis frameworks:

.. .. list-table::
..    :header-rows: 1
..    :widths: 50 50 100

..    * - language
..      - Repository
..      - Descriptions
..    * - |:coffee:|
..      - `CLIJ3 <https://github.com/clEsperanto/clij3>`_
..      - Fiji plugin
..    * - |:snake:|
..      - `napari-assistant <https://github.com/clEsperanto/napari_pyclesperanto_assistant>`_
..      - Napari plugin

- |:snake:| : `napari-assistant <https://github.com/clEsperanto/napari_pyclesperanto_assistant>`_ Napari plugin
- |:coffee:| : `CLIJ3 <https://github.com/clEsperanto/clij3>`_ Fiji plugin

How do we work together
-----------------------

clEsperanto is developed as a community effort in the open because we believe in the open source community.
Contributions like feedback, suggestions, code and testing are very welcome.
This can be done through github issue, pull requests, or via `image.sc forum <https://forum.image.sc/>`_ using the tag `clesperanto`.

The clesperanto project is maintained and lead as a `benevolent dictatorship <http://oss-watch.ac.uk/resources/benevolentdictatorgovernancemodel>`_ by `Stephane Rigaud <https://github.com/strigaud>`_ and `Robert Haase <https://github.com/haesleinhuepf>`_.

Contribution are very welcome, and do not hesitate to get in touch with us so that we can help you get started, we are happy to help!

Acknowledgements
----------------

We acknowledge support by the Deutsche Forschungsgemeinschaft under Germany's Excellence Strategy (EXC2068) Cluster of Excellence Physics of Life of TU Dresden.
This project has been made possible in part by grant number 2021-237734 (`GPU-accelerating Fiji and friends using distributed CLIJ, NEUBIAS-style, EOSS4 <https://chanzuckerberg.com/eoss/proposals/gpu-accelerating-fiji-and-friends-using-distributed-clij-neubias-style/>`_) from the Chan Zuckerberg Initiative DAF, an advised fund of the Silicon Valley Community Foundation.