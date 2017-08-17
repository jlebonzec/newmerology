""" LifePath pattern number.

It consists in the sum of the birth numbers
"""

from calculator.computations import utils
from calculator.config import POWERS


class Computation(utils.AbstractComputation):

    def run(self):
        year, month, day = self.birth.year, self.birth.month, self.birth.day
        num = utils.simplify(year + month + day)
        if num in POWERS:
            # Stop here, we found a power number
            self._result = num
        else:
            # Try another way to find the power number
            self._result = utils.simplify(
                utils.simplify(year, keep_power=False) +
                utils.simplify(month, keep_power=False) +
                utils.simplify(day, keep_power=False)
            )
        self._result = int(self._result)

        # Compute the example
        self._example = [
            self.birth.isoformat(),
            "%04d+%02d+%02d = %d" % (year, month, day, self._result)
        ]
