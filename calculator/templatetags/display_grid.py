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

from calculator.computations.grid_computation import AbstractGridComputation

from django import template


register = template.Library()


@register.inclusion_tag('helpers/display_grid.djt')
def display_grid(grid):
    """ Display a grid

    :param grid: The grid object to display
    :type grid: AbstractGridComputation

    :return: a context to display the grid in a template
    """
    return {'grid': grid.grid, 'cell_id': grid.cell_id}
