""" Third Action. See the AbstractActionComputation for how it's computed """

from calculator.computations.time_computation import AbstractActionComputation


class Computation(AbstractActionComputation):

    def __init__(self, person):
        super(AbstractActionComputation, self).__init__(person)
        self.period_id = 2
