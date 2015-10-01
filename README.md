
Two simple jinja2 extensions.

raise
-----

Raise a TemplateRuntimeError with the given error message.

Example:

    {% if x >= 3 %}{% raise "x must be less than 3" %}{% endif %}


require
-------

The `require` statement will `include` a template only if it has not been
previously required (aka, "include once"). Unlike the jinja `import`
statement, `require` allows the included template to contain content, not
just macros. We use this for code generation where we wish to require
utility functions, but there are likely other use cases as well.

Example:

    {% require "util_lib.tmpl" %}


LICENSE
=======

This software is Copyright (c) 2013 APCI, LLC.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
