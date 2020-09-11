# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2020 Stephan Linz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import os
import sphinx

# See: https://www.python.org/dev/peps/pep-0328/
# Relative imports must always use from <> import ; import <> is always
# absolute. Of course, absolute imports can use from <> import by omitting
# the leading dots.

from . import lexer

def setup(app):
    """
    @brief Main entry point for Li-Pro.Net Sphinx Primer contribution.

    Introduce:

    * additional roles, and directives
    * additional lexer for Pygments (syntax highlighting)
    * HOT FIXES

    @param app: The documentation application.
    """

    for a in lexer.DotLexer.aliases: app.add_lexer(a, lexer.DotLexer)
    for a in lexer.DtsLexer.aliases: app.add_lexer(a, lexer.DtsLexer)

    #
    # avoid WARNING: Unknown interpreted text role "confval".
    #
    # --> https://jupyter-tutorial.readthedocs.io/de/stable/
    #     --> Produkt erstellen
    #         --> Dokumentieren
    #             --> Intersphinx
    #                 --> Rollen hinzufügen
    #
    # from sphinx.ext.autodoc import cut_lines
    # app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
