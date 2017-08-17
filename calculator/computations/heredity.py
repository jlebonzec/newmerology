""" Heredity number.

It consists in the mapped sum of the last name
"""

from calculator.computations import utils


class Computation(utils.AbstractComputation):

    def run(self):
        digits = utils.digitize(self.last_name)

        self._result = utils.simplify(digits)
        self._example = utils.examplify(self.last_name, digits, self._result)
