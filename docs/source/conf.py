# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os,sys

sys.path.insert(0, os.path.abspath("../exo/"))
print(sys.executable)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'exo'
copyright = '2024, exo-labs'
author = 'exo-labs'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx.ext.intersphinx",
  "sphinx.ext.autodoc",
  "sphinx.ext.napoleon",
  "sphinx.ext.viewcode",
  "sphinx_autodoc_typehints",
]

intersphinx_mapping = {
  "python": ("https://docs.python.org/3", None),
  "numpy": ("https://numpy.org/doc/stable/", None),
}

napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
