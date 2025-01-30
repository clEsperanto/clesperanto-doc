# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import re
import sys
import time
from pathlib import Path

from sphinx.locale import _

def setup(app):
    app.add_css_file('custom.css')

year = time.localtime().tm_year

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'clEsperanto'
slug = re.sub(r"\W+", "-", project.lower())
author = 'clEsperanto authors'
copyright = f"2020-{year}, clEsperanto authors"
release = '0.16.0'

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

html_theme_options = {
    "light_logo": "logo_w.svg",
    "dark_logo": "logo_d.svg",
    "sidebar_hide_name": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/clEsperanto",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

