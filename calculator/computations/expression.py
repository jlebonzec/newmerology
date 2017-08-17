""" Expression number.

It consists in the mapped sum of the given names and last name
"""

from calculator.computations import utils


class Computation(utils.AbstractComputation):

    def run(self):
        digits = utils.string_to_digits(self.full_name)

        self._result = utils.simplify(digits)
        self._example = utils.conversion_to_example(self.full_name, digits, self._result)
