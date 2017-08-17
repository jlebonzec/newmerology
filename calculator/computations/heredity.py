""" Heredity number.

It consists in the mapped sum of the last name
"""

from calculator.computations import utils


class Computation(utils.AbstractComputation):

    def run(self):
        digits = utils.string_to_digits(self.last_name)

        self._result = utils.simplify(digits)
        self._example = utils.conversion_to_example(self.last_name, digits, self._result)
