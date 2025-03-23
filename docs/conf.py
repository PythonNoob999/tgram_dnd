# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
sys.path.insert(0, os.path.abspath(".."))

project = 'TgramDND'
copyright = '2025, SpicyPenguin'
author = 'SpicyPenguin'
release = '0.0.5b'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.napoleon", "sphinxcontrib.googleanalytics"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
googleanalytics_id = os.environ["GA_ID"]
autodoc_type_aliases = {
    "LANGUAGE_CODES": "tgram_dnd.enums.language_codes.LANGUAGE_CODES",
    "REPLY_METHODS": "tgram_dnd.enums.reply_methods.REPLY_METHODS",
}
html_static_path = ['_static']