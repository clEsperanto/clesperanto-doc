# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import importlib
import inspect
import os
import re
import sys
import time
import warnings
from pathlib import Path

import sphinx.domains.cpp
from sphinx.domains import ObjType
from sphinx.util.docutils import SphinxDirective

warnings.filterwarnings(
    "ignore",
    message=".*No pyclesperanto backend.*",
    category=RuntimeWarning,
)

warnings.filterwarnings(
    "ignore",
    message=".*No pyclesperanto backend.*",
)

from sphinx.locale import _

def get_version():
    # pinned clEsperanto version documented by this build, None for development branches
    # (same logic as scripts/fetch_sources.sh)
    version = os.environ.get("CLESPERANTO_VERSION")
    if not version and os.environ.get("READTHEDOCS_VERSION_TYPE") == "tag":
        version = os.environ.get("READTHEDOCS_GIT_IDENTIFIER", "").removeprefix("v")
    return version or None


def get_source_refs():
    # refs actually cloned by scripts/fetch_sources.sh (patch versions may differ between repos)
    refs_file = Path("_submodules/refs.txt")
    if not refs_file.exists():
        return {}
    lines = refs_file.read_text().splitlines()
    return dict(line.split("=", 1) for line in lines if "=" in line)


clesperanto_version = get_version()
pyclesperanto_tag = get_source_refs().get("pyclesperanto", "main")


def replace_version_placeholders(app, docname, source):
    # roles and substitutions are not processed in raw html blocks, so we replace placeholders directly
    source[0] = source[0].replace("{{ pyclesperanto_tag }}", pyclesperanto_tag)


def setup(app):
    app.add_css_file('custom.css')
    app.connect('source-read', replace_version_placeholders)
    app.connect('builder-inited', prepare_pyclesperanto)
    app.add_directive('pyclesperanto-api', PyclesperantoAPI)
    app.add_domain(CPPDomain, override=True)

year = time.localtime().tm_year

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'clEsperanto'
slug = re.sub(r"\W+", "-", project.lower())
author = 'clEsperanto authors'
copyright = f"2020-{year}, clEsperanto authors"
release = clesperanto_version or "latest"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinxext.opengraph',
    'sphinx.ext.extlinks',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinx_inline_tabs',
    'breathe',
    'sphinxemoji.sphinxemoji',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.pixi', '_submodules']

todo_include_todos = True

# -- External links (version dependent) ----------------------------------------
# usage: :pycle-demo:`Link title <api/select_devices.ipynb>`

extlinks = {
    'pycle-demo': (f'https://github.com/clEsperanto/pyclesperanto/blob/{pyclesperanto_tag}/docs/demos/%s', '%s'),
}

# -- pyclesperanto auto-documentation ----------------------------------------
from unittest.mock import MagicMock

sys.modules['pyclesperanto._pyclesperanto'] = MagicMock()
sys.modules['pyclesperanto_opencl'] = MagicMock()
sys.modules['pyclesperanto_opencl._pyclesperanto'] = MagicMock()

sys.path.insert(0, str(Path('.', '_submodules/pyclesperanto').resolve()))
autodoc_mock_imports = [
    "pyclesperanto._pyclesperanto",
    "pyclesperanto_opencl._pyclesperanto",
    "matplotlib",
    "numpy",
]
add_module_names = False


def prepare_pyclesperanto(app):
    # import pyclesperanto once with the mocked dependencies, and give it a documentable Array:
    # cle.Array is a proxy whose methods are patched at runtime onto the backend array class,
    # so we patch them onto a plain class instead
    from sphinx.ext.autodoc.mock import mock

    with mock(autodoc_mock_imports):
        import pyclesperanto
        from pyclesperanto import _array

        class Array:
            __doc__ = _array.Array.__doc__
            __module__ = "pyclesperanto"

            def reshape(self, *shape):  # replaced by _patch_array_class
                pass

        get_array_class = _array._get_array_class
        _array._get_array_class = lambda: Array
        try:
            _array._patch_array_class()
        finally:
            _array._get_array_class = get_array_class
        pyclesperanto.Array = Array


def defined_in(obj, module_name):
    # follow the functools.wraps chain (plugin_function, deprecated) to the original definition
    try:
        return inspect.unwrap(obj).__module__ == module_name
    except (ValueError, AttributeError):
        return False


class PyclesperantoAPI(SphinxDirective):
    """Document the objects of a private pyclesperanto module under their public name.

    ``.. pyclesperanto-api:: pyclesperanto._tier1`` documents ``pyclesperanto.absolute``
    instead of ``pyclesperanto._tier1.absolute``, so that the search and cross-references
    use the names users actually call (``cle.absolute``).
    """

    required_arguments = 1

    def run(self):
        import pyclesperanto

        module = importlib.import_module(self.arguments[0])
        lines = []
        for name, obj in sorted(vars(module).items()):
            if name.startswith("_") or getattr(pyclesperanto, name, None) is not obj:
                continue
            if not defined_in(obj, module.__name__):
                continue
            if inspect.isclass(obj):
                lines += [f".. autoclass:: pyclesperanto.{name}", "    :members:", ""]
            else:
                lines += [f".. autofunction:: pyclesperanto.{name}", ""]
        return self.parse_text_to_nodes("\n".join(lines))


JAVA_OBJECT_TYPES = {
    "class": ObjType("class", "class"),
    "function": ObjType("method", "func"),
    "enum": ObjType("enum", "enum"),
    "enumerator": ObjType("enum constant", "enumerator"),
}


class CPPDomain(sphinx.domains.cpp.CPPDomain):
    # Adjust how C++ objects (CLIc and clesperantoj, both parsed by breathe) appear in the search:
    # - function and template parameters are left out: they are still rendered, but otherwise every
    #   "device", "src" or "sigma_x" of every C++ and Java function is a search hit
    # - clesperantoj objects are listed as Java ("Java method", net.clesperanto.kernels.Tier1.gaussianBlur)
    #   instead of C++ ("C++ function", net::clesperanto::kernels::Tier1::gaussianBlur)
    object_types = sphinx.domains.cpp.CPPDomain.object_types | {
        f"java_{name}": objtype for name, objtype in JAVA_OBJECT_TYPES.items()
    }

    def get_type_name(self, type, primary=False):
        if type in JAVA_OBJECT_TYPES.values():
            return type.lname if primary else f"Java {type.lname}"
        return super().get_type_name(type, primary)

    def get_objects(self):
        for name, dispname, objtype, docname, anchor, priority in super().get_objects():
            if objtype in ("functionParam", "templateParam"):
                continue
            if docname.startswith("docs/clesperantoj/") and objtype in JAVA_OBJECT_TYPES:
                objtype = f"java_{objtype}"
                dispname = dispname.replace("::", ".")
            yield name, dispname, objtype, docname, anchor, priority

# -- CLIc and auto-documentation -------------------------------------------------

sys.path.insert(0, str(Path('.', '_submodules/clesperantoj').resolve()))

breathe_projects = {
    'CLIc': './_submodules/clic/docs/build/doxygen/xml',
    'clesperantoj': './_submodules/clesperantoj/docs/xml',
    }
breathe_default_project = 'CLIc'
breathe_domain_by_extension = {'h': 'cpp', 'hpp': 'cpp'}
cpp_index_common_prefix = [
    'cle::',
    'cle::tier1::',
    'cle::tier2::',
    'cle::tier3::',
    'cle::tier4::',
    'cle::tier5::',
    'cle::tier6::',
    'cle::tier7::',
    'cle::tier8::',
    ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo' #'sphinx_immaterial' #'furo' #sphinx_rtd_theme
html_title = "clEsperanto"
html_favicon = './_static/favicon.ico'
pygments_style = "sphinx"
pygments_dark_style = "monokai"

html_static_path = ['_static']

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme_options = {
    "light_logo": "logo_w.svg",
    "dark_logo": "logo_d.svg",
    "sidebar_hide_name": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/pradyunsg/furo",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

html_search_options = {
    'type': 'default',
}

