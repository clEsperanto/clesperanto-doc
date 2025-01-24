# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import re
import sys
from pathlib import Path


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'clEsperanto'
slug = re.sub(r"\W+", "-", project.lower())
author = 'clEsperanto authors'
copyright = f"2020-2025, clEsperanto authors"
release = '0.16.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.pixi', '_submodules']


# -- pyclesperanto auto-documentation ----------------------------------------
sys.path.insert(0, str(Path('.', '_submodules/pyclesperanto').resolve()))
autodoc_mock_imports = ["pyclesperanto._pyclesperanto", "toolz", "matplotlib", "numpy"]


# -- CLIc auto-documentation -------------------------------------------------
breathe_projects = {'CLIc': './_submodules/clic/docs/build/doxygen/xml'}
breathe_default_project = 'CLIc'
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

html_theme = 'sphinx_rtd_theme'
# html_theme_options = {
#     "logo_only": False,
#     "title_only": False,
#     "navigation_depth": 5,
#     "collapse_navigation": False,
#     "sticky_navigation": True,
#     "version_selector": True,
# }

html_static_path = ['_static']
