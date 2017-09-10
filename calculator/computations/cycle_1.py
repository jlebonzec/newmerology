""" First Cycle. See the AbstractCycleComputation for how it's computed """

from calculator.computations.time_computation import AbstractCycleComputation


class Computation(AbstractCycleComputation):

    def __init__(self, person):
        super(AbstractCycleComputation, self).__init__(person)
        self.period_id = 0
