""" Psychic number.

It consists in the simplification of the day of birth
"""

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        digits = self.birth.day

        self._result = utils.simplify(digits)
        self._example = utils.examplify(self.birth.isoformat(), digits, self._result)
