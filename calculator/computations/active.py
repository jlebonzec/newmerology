""" Active number.

It consists in the mapped sum of the given names
"""

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        digits = utils.digitize(self.given_names)

        self._result = utils.simplify(digits)
        self._example = utils.examplify(self.given_names, digits, self._result)
