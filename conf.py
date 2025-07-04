# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import re
import sys
import time
from pathlib import Path

from sphinx.locale import _


def parse_version():

    # read the file ".readthedocs.yaml" and parse to find all version numbers
    with open(".readthedocs.yaml", "r") as f:
        content = f.read()
        versions = re.findall(r"(\d+\.\d+\.\d+)", content)

    # make a commont version number which is the combination of the lowest values in the list
    if versions:
        major = min(int(v.split('.')[0]) for v in versions)
        minor = min(int(v.split('.')[1]) for v in versions if int(v.split('.')[0]) == major)
        patch = min(int(v.split('.')[2]) for v in versions if int(v.split('.')[0]) == major and int(v.split('.')[1]) == minor)
        common_version = f"{major}.{minor}.{patch}"

    return common_version


def setup(app):
    app.add_css_file('custom.css')

year = time.localtime().tm_year

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'clEsperanto'
slug = re.sub(r"\W+", "-", project.lower())
author = 'clEsperanto authors'
copyright = f"2020-{year}, clEsperanto authors"
release = parse_version()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinxext.opengraph',
    'sphinx_inline_tabs',
    'breathe',
    'sphinxemoji.sphinxemoji',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.pixi', '_submodules']

todo_include_todos = True

# -- pyclesperanto auto-documentation ----------------------------------------
sys.path.insert(0, str(Path('.', '_submodules/pyclesperanto').resolve()))
autodoc_mock_imports = ["pyclesperanto._pyclesperanto", "toolz", "matplotlib", "numpy"]
add_module_names = False


# -- CLIc auto-documentation -------------------------------------------------
breathe_projects = {'CLIc': './_submodules/clic/docs/build/doxygen/xml'}
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

html_theme = 'furo' #sphinx_rtd_theme
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
            "url": "https://github.com/clEsperanto/",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

