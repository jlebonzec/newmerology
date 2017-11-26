#   This file is part of Newmerology.
#
#   Newmerology is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Newmerology is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with Newmerology.  If not, see <https://www.gnu.org/licenses/agpl.html>.

from django import template
from django_translate.services import tranz


register = template.Library()


@register.inclusion_tag('helpers/months_full.djt')
def months_full():
    """ Display the full name of months for JS, translated
    """
    prefix = 'g.months.full.'
    months = []
    for i in range(1, 13):
        month_name = prefix + str(i)
        months.append(tranz(month_name))
    return {'months': months}
