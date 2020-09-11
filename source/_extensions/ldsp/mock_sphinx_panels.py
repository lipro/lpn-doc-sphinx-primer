# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Stephan Linz
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

from sphinx.directives import code
from docutils.parsers.rst import directives, roles

class DirectiveAsCodeBlock(code.CodeBlock):

    has_content = True
    required_arguments = 0
    optional_arguments = 0

    # mock all options that the admonition not have
    option_spec = code.CodeBlock.option_spec.copy()
    option_spec['type'] = directives.unchanged
    option_spec['text'] = directives.unchanged
    option_spec['tooltip'] = directives.unchanged
    option_spec['classes'] = directives.unchanged
    option_spec['container'] = directives.unchanged
    option_spec['title'] = directives.unchanged
    option_spec['header'] = directives.unchanged
    option_spec['body'] = directives.unchanged
    option_spec['footer'] = directives.unchanged
    option_spec['open'] = directives.flag
    option_spec['name'] = directives.unchanged
    option_spec['animate'] = directives.unchanged
    option_spec['column'] = directives.unchanged
    option_spec['card'] = directives.unchanged
    option_spec['img-top-cls'] = directives.unchanged
    option_spec['img-bottom-cls'] = directives.unchanged

def setup(app):
    """
    @brief Main entry point for the Sphinx Panels mocking.
    @param app: The documentation application.
    """
    logger = sphinx.util.logging.getLogger(__name__)

    app.add_directive("link-button", DirectiveAsCodeBlock)
    app.add_directive("dropdown", DirectiveAsCodeBlock)
    app.add_directive("panels", DirectiveAsCodeBlock)
    app.add_directive("div", DirectiveAsCodeBlock)

    app.add_role("link-badge", roles.generic_custom_role)
    app.add_role("badge", roles.generic_custom_role)
    app.add_role("opticon", roles.generic_custom_role)
    app.add_role("fa", roles.generic_custom_role)

    logger.info('{} extension active!'.format(__name__), color='blue')
