# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Stephan Linz
# Copyright (c) 2017 Adam Szmyd <szmydadam@gmail.com>
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

# https://github.com/sphinx-doc/sphinx/issues/4054#issuecomment-329097229
# https://stackoverflow.com/a/40264720
def ultimateReplace(app, docname, source):
    result = source[0]
    for key in app.config.ultimate_replacements:
        value = app.config.ultimate_replacements[key]
        result = result.replace(key, value)
    source[0] = result

def setup(app):
    """
    @brief Using variables inside reST w/o 'rst_prolog' or 'rst_epilog'.
    @param app: The documentation application.
    """
    logger = sphinx.util.logging.getLogger(__name__)

    app.add_config_value('ultimate_replacements', {}, True)
    app.connect('source-read', ultimateReplace)

    logger.info('{} extension active!'.format(__name__), color='blue')
