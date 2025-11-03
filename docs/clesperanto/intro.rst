The clesperanto project
#######################

The clesperanto project is a multi-language and multi-platform framework for GPU-accelerated image processing.
It aims at removing language barriers in the scientific image analysis community by proposing a unified interface API for different programming languages and frameworks, which rely on a common backend library accelerated by GPU.

The project is organised in a set of core-repository APIs, each dedicated to a programming language, and a set of plugins or assistants targeting the main BioImage Analysis frameworks (Fiji, Napari, etc.).

The core-repository APIs are composed of the following repositories:

- |:rocket:| : `CLIc <https://github.com/clEsperanto/CLIc>`_ C++ API & project backend
- |:snake:| : `pyclesperanto <https://github.com/clEsperanto/pyclesperanto>`_ Python API
- |:coffee:| : `clesperantoJ <https://github.com/clEsperanto/clesperantoj_prototype>`_ Java API

and a set of satellite repositories which embed the core API into the main BioImage Analysis frameworks:

- |:snake:| : `napari-assistant <https://github.com/clEsperanto/napari_pyclesperanto_assistant>`_ Napari plugin
- |:coffee:| : `CLIJ3 <https://github.com/clEsperanto/clij3>`_ Fiji plugin

