""" Psychic number.

It is the day of birth (the day in the month, i.e. 1-31)
"""

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        digits = self.birth.day

        self._result = digits
        self._example = utils.examplify(self.birth.isoformat(), digits, self._result)
