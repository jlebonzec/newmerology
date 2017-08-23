""" Expression number.

It consists in the mapped sum of the given names and last name
"""

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        digits = utils.digitize(self.full_name)

        self._result = utils.simplify(digits)
        self._example = utils.examplify(self.full_name, digits, self._result)
