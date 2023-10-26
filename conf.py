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
"sphinx_design",
'sphinx_sitemap',
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

html_static_path = ['_static']

html_extra_path = ["_extra"]

# ---------------------------- Theme PyData

html_theme = 'pydata_sphinx_theme'

def setup(app):
    app.add_css_file("custom.css")
    app.add_js_file("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2719430950228844",loading_method="async")

html_sidebars = {
    "index": ["aboutme.html",'tagcloud.html'],
    "sobre-mi":["sidebar-nav-bs"],
    "recursos-gratis/**":["sidebar-nav-bs"],
    "cursos": ["aboutme.html",'tagcloud.html'],
    "sgb": ["aboutme.html",  "recentposts.html", "archives.html"],
    "blog":["aboutme.html", "categories.html", "tagcloud.html", "archives.html"],
    "posts/**": ["aboutme.html", 'postcard.html'],
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    'css/custom.css',
]

html_theme_options = {
    "show_prev_next": True,
    "analytics": {"google_analytics_id": "G-X0SW72PREQ"},
    "logo": {
      "image_light": "_static/images/logo.png",
      "image_dark": "_static/images/logo-dark.png",
   },
   "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/luis575497",
            "icon": "fab fa-github fa-xl",
            "type": "fontawesome",
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0001-7921-4228",
            "icon": "fa-brands fa-orcid fa-2xl",
            "type": "fontawesome",
        },
    ],
    "announcement": '¡Potencia tu carrera con nuestros <a href="https://luis575497.github.io/cursos/">cursos de biblioteca</a> en BiblioBytes! 📚💡',
}

html_context = {
   "default_mode": "dark"
}

# ---------------------------------------- Ablog
blog_feed_templates = {
      # Use defaults, no templates
      "atom": {},
      # Create content text suitable posting to social media
      "social": {
         # Format tags as hashtags and append to the content
         "content": "{{ title }}{% for tag in post.tags %}"
         " #{{ tag.name|trim()|replace(' ', '') }}"
         "{% endfor %}",
      },
}

github_pages = "luis575497"
blog_feed_archivos = True
myst_update_mathjax = False
disqus_shortname = "bibliobytes"
blog_baseurl = "https://luis575497.github.io/"


# ------------------------------------------ SiteXML
html_baseurl = "https://luis575497.github.io/"
