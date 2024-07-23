# MIT License
#
# Copyright (c) 2024 Andrey Rybakov (rybakov.ad@icloud.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from datetime import datetime
from os.path import abspath


sys.path.insert(0, abspath("."))


##########################################################################################
##                                   Project metadata                                   ##
##########################################################################################

version = "alpha"
project = "Plotting with Python"
author = "Andrey Rybakov"
copyright = f"2024-{datetime.now().year}, {author}"


##########################################################################################
##                                      Extensions                                      ##
##########################################################################################
extensions = [
    "sphinx.ext.duration",  # Measure the time of the build
    "sphinx.ext.extlinks",  # Markup to shorten external links
    "sphinx_copybutton",  # Copybutton for the blocks
    "sphinx.ext.intersphinx",  # Link to other projects’ documentation
    "sphinx_design",  # For dropdowns
]

##########################################################################################
##                                  Build configuration                                 ##
##########################################################################################

smartquotes = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

##########################################################################################
##                                Options for HTML output                               ##
##########################################################################################
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["plotting-with-python.css"]

html_title = f"{project} {version}"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#198F88",
        "color-code-background": "#E6E6E6",
    },
    "dark_css_variables": {
        "color-brand-primary": "#7BC4AC",
    },
    "source_repository": "https://github.com/adrybakov/plotting-with-python",
    "source_branch": "main",
    "source_directory": "docs/",
    "top_of_page_button": "edit",
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/adrybakov/plotting-with-python",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/adrybakov",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M16,2.8724 C15.411,3.1337 14.779,3.3097 14.115,3.3891 C14.792,2.9831 15.313,2.3397 15.558,1.5731 C14.924,1.9497 14.221,2.2224 13.47,2.3704 C12.875,1.7317 12.021,1.3331 11.077,1.3331 C9.265,1.3331 7.795,2.8031 7.795,4.6157 C7.795,4.8731 7.824,5.1237 7.88,5.3637 C5.152,5.2271 2.733,3.9204 1.114,1.9337 C0.831,2.4191 0.669,2.9824 0.669,3.5844 C0.669,4.7231 1.249,5.7284 2.130,6.3171 C1.592,6.2991 1.085,6.1517 0.643,5.9064 L0.643,5.9471 C0.643,7.5377 1.774,8.8644 3.276,9.1657 C3.001,9.2417 2.710,9.2811 2.411,9.2811 C2.199,9.2811 1.994,9.2604 1.79,9.2224 C2.211,10.5264 3.423,11.4757 4.86,11.5024 C3.736,12.3824 2.321,12.9071 0.783,12.9071 C0.518,12.9071 0.257,12.8917 0,12.8617 C1.453,13.7924 3.178,14.3364 5.032,14.3364 C11.070,14.3364 14.371,9.3344 14.371,4.9964 C14.371,4.8544 14.368,4.7131 14.362,4.5724 C15.003,4.1091 15.56,3.5311 16,2.8724"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}


##########################################################################################
##              Custom variables with access from .rst files and docstrings             ##
##########################################################################################
variables_to_export = [
    "project",
    "copyright",
    "version",
]

frozen_locals = dict(locals())
rst_epilog = "\n".join(
    map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export)
)
del frozen_locals

##########################################################################################
##                                Dynamic external links                                ##
##########################################################################################
# Usage :numpy:`ndarray`
extlinks = {
    "numpy": (
        "https://numpy.org/doc/stable/reference/generated/numpy.%s.html",
        "numpy.%s",
    ),
    "matplotlib": (
        "https://matplotlib.org/stable/api/%s_api.html",
        "matplotlib.%s",
    ),
}

##########################################################################################
##                                 Static external links                                ##
##########################################################################################

# Solution source:
# https://docutils.sourceforge.io/docs/ref/rst/directives.html#directives-for-substitution-definitions
# Usage: |Python|_
custom_links = {
    "Python": ("Python", "https://python.org"),
    "NumPy": ("NumPy", "https://numpy.org/"),
    "SciPy": ("SciPy", "https://scipy.org/"),
    "matplotlib": ("matplotlib", "https://matplotlib.org/"),
    "reserved-keywords": (
        "reserved keywords",
        "https://docs.python.org/3/reference/lexical_analysis.html#keywords",
    ),
    "Python-print": (
        "print()",
        "https://docs.python.org/3/library/functions.html#print",
    ),
    "Numpy-loadtxt": (
        "numpy.loadtxt()",
        "https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html",
    ),
    "Numpy-savetxt": (
        "numpy.load()",
        "https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html",
    ),
    "Numpy-math": (
        "Mathematical functions",
        "https://numpy.org/doc/stable/reference/routines.math.html",
    ),
    "Numpy-user-guide": (
        "NumPy user guide",
        "https://numpy.org/doc/stable/user/index.html",
    ),
    "Numpy-basics": (
        "absolute basics for beginners",
        "https://numpy.org/doc/stable/user/absolute_beginners.html",
    ),
    "matplotlib-user-guide": (
        "matplotlib user guide",
        "https://matplotlib.org/stable/users/index.html",
    ),
    "matplotlib-quickstart": (
        "quickstart guide",
        "https://matplotlib.org/stable/users/explain/quick_start.html",
    ),
    "matplotlib-subplots": (
        "plt.subplots()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html",
    ),
    "matplotlib-layout": (
        "Arranging multiple Axes in a Figure",
        "https://matplotlib.org/stable/users/explain/axes/arranging_axes.html",
    ),
    "matplotlib-plot": (
        "ax.imshow()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html",
    ),
    "matplotlib-scatter": (
        "ax.imshow()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html",
    ),
    "matplotlib-imshow": (
        "ax.imshow()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html",
    ),
    "ax-set-xlabel": (
        "ax.set_xlabel()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html",
    ),
    "ax-set-ylabel": (
        "ax.set_ylabel()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html",
    ),
    "ax-legend": (
        "ax.legend()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html",
    ),
    "ax-set-ticks": (
        "ax.set_ticks()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ticks.html",
    ),
    "ax-ticks-params": (
        "ax.ticks_params()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticks_params.html",
    ),
    "ax-set-title": (
        "ax.set_title()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html",
    ),
    "ax-text": (
        "ax.text()",
        "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html",
    ),
}

rst_epilog += "\n".join(
    map(
        lambda x: f"\n.. |{x}| replace:: {custom_links[x][0]}\n.. _{x}: {custom_links[x][1]}",
        [i for i in custom_links],
    )
)
