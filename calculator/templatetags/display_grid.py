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
