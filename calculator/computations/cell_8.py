""" Eighth cell of the grid. See the AbstractGridComputation for how it's computed """

from calculator.computations.grid_computation import AbstractGridComputation


class Computation(AbstractGridComputation):

    def __init__(self, *args, **kwargs):
        super(Computation, self).__init__(*args, **kwargs)
        self.cell_id = 8
