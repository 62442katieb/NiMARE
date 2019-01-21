#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NiMARE documentation build configuration file, created by
# sphinx-quickstart
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('sphinxext'))
sys.path.insert(0, os.path.abspath('../nimare'))

from github_link import make_linkcode_resolve


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

# needs_sphinx = '1.0'

# generate autosummary even if no references
autosummary_generate = True
autodoc_default_flags = ['members', 'inherited-members']
add_module_names = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinxarg.ext',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosummary',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'numpydoc',
              'sphinx.ext.ifconfig',
              'sphinx.ext.linkcode',
              'sphinx_gallery.gen_gallery',
              'sphinx_click.ext']

import sphinx
from distutils.version import LooseVersion
if LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.append('sphinx.ext.pngmath')
else:
    extensions.append('sphinx.ext.imgmath')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = 'NiMARE'
copyright = '2018, NiMARE developers'
author = 'NiMARE developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import nimare
version = nimare.__version__
# The full version, including alpha/beta/rc tags.
release = nimare.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'utils/*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# installing theme package

#import sphinx_rtd_theme

html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

html_style = 'nimare.css'
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'searchbox.html', 'indexsidebar.html'] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# https://github.com/rtfd/sphinx_rtd_theme/issues/117
def setup(app):
    app.add_stylesheet('theme_overrides.css')
    app.connect('autodoc-process-docstring', generate_example_rst)

html_favicon = '_static/nimare_favicon.png'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'nimaredoc'

# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve('nimare',
                                         u'https://github.com/neurostuff/'
                                         'nimare/blob/{revision}/'
                                         '{package}/{path}#L{lineno}')

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'http://docs.python.org/3.5': None,
    'http://docs.scipy.org/doc/numpy': None,
    'http://docs.scipy.org/doc/scipy/reference': None,
    'http://matplotlib.org/': None,
    'http://scikit-learn.org/0.17': None,
    'http://nipy.org/nibabel/': None,
    'http://pandas.pydata.org/pandas-docs/stable/': None,
}

sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs'     : '../examples',
    # path where to save gallery generated examples
    'gallery_dirs'      : 'auto_examples',
    'backreferences_dir': '_build/backreferences',
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    'doc_module'        : ('nimare'),
    'ignore_patterns'   : ['utils/'],
    }

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'project-template', u'project-template Documentation',
   u'Vighnesh Birodkar', 'project-template', 'One line description of project.',
   'Miscellaneous'),
]

def generate_example_rst(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    folder = os.path.join(app.srcdir, 'generated')
    if not os.path.isdir(folder):
        os.makedirs(folder)
    examples_path = os.path.join(app.srcdir, "generated",
                                 "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, 'w').close()

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
