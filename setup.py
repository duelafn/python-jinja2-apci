#!/usr/bin/env python
"""
APCI LLC's jinja2 extensions
"""
# Author: Dean Serenevy  <deans@apcisystems.com>
# This software is Copyright (c) 2013 APCI, LLC.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import re

__version__ = re.search(r'(?m)^__version__\s*=\s*"([\d.]+(?:[\-\+~.]\w+)*)"', open('jinja2_apci/__init__.py').read()).group(1)

from distutils.core import setup

setup(
    name         = 'jinja2-apci',
    version      = __version__,
    url          = 'http://apcisystems.com/',
    author       = "APCI LLC",
    author_email = 'deans@apcisystems.com',
    description  = "Jinja2 Extensions: raise and require",
    packages     = [ 'jinja2_apci' ],
    provides     = "jinja_apci",
    requires     = [ "jinja2", ],
)
