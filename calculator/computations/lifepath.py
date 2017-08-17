""" LifePath pattern number.

It consists in the sum of the birth numbers
"""

from calculator.computations import utils
from calculator.config import POWERS


class Computation(utils.AbstractComputation):

    def run(self):
        year, month, day = self.birth.year, self.birth.month, self.birth.day
        num = utils.simplify(year + month + day)
        if num not in POWERS:
            # Try another way to find the power number
            num = utils.simplify(
                utils.simplify(year, keep_power=False) +
                utils.simplify(month, keep_power=False) +
                utils.simplify(day, keep_power=False)
            )
        self._result = num

        # Compute the example
        formatted_birth = self.birth.isoformat()
        formatted_sum = "%04d+%02d+%02d" % (year, month, day)
        self._example = utils.examplify(formatted_birth, formatted_sum, self._result)
