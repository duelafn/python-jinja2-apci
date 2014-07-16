# -*- coding: utf-8 -*-
""" Jinja extension which provides "require" statement

The `require` statement will `include` a template only if it has not been
previously required (aka, "include once"). Unlike the jinja `import`
statement, `require` allows the included template to contain content, not
just macros. We use this for code generation where we wish to require
utility functions, but there are likely other use cases as well.
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
__all__ = [ 'RequireExtension' ]

from jinja2 import nodes
from jinja2.ext import Extension

# See: http://jinja.pocoo.org/docs/extensions/#example-extension
class RequireExtension(Extension):
    # This is our keyword(s):
    tags = set(['require'])

    def __init__(self, environment):
        super(RequireExtension, self).__init__(environment)
        # Define the attr we will use
        environment.extend(require_seen=set())


    # See also: jinja2.parser.parse_include()
    def parse(self, parser):
        # the first token is the token that started the tag. In our case we
        # only listen to "require" so this will be a name token with
        # "require" as value. We get the line number so that we can give
        # that line number to the nodes we insert.
        lineno = next(parser.stream).lineno

        # Create an Include node, giving it our lineno and the next
        # expression which will be the template name to include. "require"
        # will not tolerate missing inclusions ever.
        include = nodes.Include(lineno=lineno)
        include.template = parser.parse_expression()
        include.ignore_missing = False

        # No matter what, we should continue here (since there may be
        # additional tokens that need to be removed).
        node = parser.parse_import_context(include, True)

        # Ensure the current file is marked as "seen" to avoid loops (to
        # pick up the entry template or any templates included through
        # other means - a bad idea, but may happen).
        self.environment.require_seen.add(parser.name)

        # However, if we've already seen the template, just return an empty node.
        name = include.template.as_const()
        if name in self.environment.require_seen:
            return nodes.CallBlock(
                self.call_method('_blank', [], lineno=lineno),
                [], [], [], lineno=lineno
            )
        else:
            self.environment.require_seen.add(name)
            return node

    def _blank(self, caller):
        return ""
