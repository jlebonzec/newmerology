""" Second cell of the grid. See the AbstractGridComputation for how it's computed """

from calculator.computations import utils


class Computation(utils.AbstractGridComputation):

    def __init__(self, *args, **kwargs):
        super(Computation, self).__init__(*args, **kwargs)
        self.cell_id = 2
