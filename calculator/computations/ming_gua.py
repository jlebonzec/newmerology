""" Ming Gua number.

Based on birth and gender.
See full explanations there: https://www.astrologjia.com/ming-gua-number.html
"""

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        if self.gender == 'O':
            self._result = 0
            self._example = "Unknown computation for non-binary genders."
            # FIXME: Translate error.
            return

        # TODO: How to find Chinese new year's day of this year?
        self.gender
        self.birth.year
        self.birth.month
        self.birth.day
        if self.gender == 'F':
            pass
        else:  # Masculine
            pass
