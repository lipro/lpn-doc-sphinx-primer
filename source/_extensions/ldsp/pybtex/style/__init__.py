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

# See: https://www.python.org/dev/peps/pep-0420/
# Namespace packages are a mechanism for splitting a single Python package
# across multiple directories on disk which serves only as a container for
# subpackages. Namespace packages may have no physical representation, and
# specifically are not like a regular package because they will have no
# __init__.py file in Python 3.
# Python currently still provides the pkgutil.extend_path to denote a package
# as a namespace package. The recommended way of using it is to put:

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

# Every distribution needs to provide the same contents in its __init__.py,
# so that extend_path is invoked independent of which portion of the package
# gets imported first. As a consequence, the package's __init__.py cannot
# practically define any names as it depends on the order of the package
# fragments on sys.path which portion is imported first. As a special feature,
# extend_path reads files named <packagename>.pkg which allow to declare
# additional portions.

# See: https://www.python.org/dev/peps/pep-0328/
# Relative imports must always use from <> import ; import <> is always
# absolute. Of course, absolute imports can use from <> import by omitting
# the leading dots.

from . import formatting
