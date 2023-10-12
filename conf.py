# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BiblioBytes'
copyright = '2023, Luis Enrique Lescano'
author = 'Luis Enrique Lescano'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
"ablog",
"sphinx.ext.intersphinx",
"sphinx_panels",
"myst_parser",
]

templates_path = ['_templates']

exclude_patterns = [
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
]

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
myst_update_mathjax = False

def setup(app):
    app.add_css_file("custom.css")

html_sidebars = {
    "index": ["aboutme.html",'tagcloud.html'],
    "sgb": ["socials.html",  "recentposts.html", "archives.html"],
    "posts/**": ["socials.html", 'postcard.html'],
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

html_theme_options = {
    "logo": {
        "text": "BiblioBytes",
    },
    "show_prev_next": True,
}

github_pages = "luis575497"