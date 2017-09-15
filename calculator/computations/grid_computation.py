""" Contains the Abstract class used for grid computation (represented as grids).
"""

from django.core.cache import cache

from calculator.computations.utils import (AbstractBaseComputation,
                                           count_occurrences,
                                           digitize,
                                           examplify)


class AbstractGridComputation(AbstractBaseComputation):
    """ AbstractGridComputation represents the computation of a cell in the grid.

    Because of how the display of the grid work, we have to compute the grid for every cell.
    Despite this operation being pretty fast (9 cells maximum), caching it avoids unnecessary work.

    :type person: models.Person
    """

    def __init__(self, person):
        super(AbstractGridComputation, self).__init__(person)
        self.cell_id = None
        self.width = 3
        self.height = 3

        cache_prefix = "person_grid_"
        self._cache_key = cache_prefix + str(person.pk)
        self._grid = cache.get(self._cache_key, {})

    @property
    def grid(self):
        """ Generate the grid if needed and return it """
        if not self._grid:
            self._grid = {}
            digits = digitize(self.full_name)

            size = self.width * self.height + 1
            for i in range(1, size):
                count, explanation = count_occurrences(digits, i, explain=True)
                example = examplify(self.full_name, explanation, count)

                self._grid[i] = {
                    'count': count,
                    'example': example,
                }

            cache.set(self._cache_key, self._grid)
        return self._grid

    def run(self):
        if self.cell_id is None:
            raise ValueError("Set a cell_id to compute the results")

        self._result = self.grid[self.cell_id]['count']
        self._example = self.grid[self.cell_id]['example']
