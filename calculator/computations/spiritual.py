""" Spiritual number.

It consists in the mapped sum of the vowels of the full name
"""

from calculator.computations import utils

import re


class Computation(utils.AbstractComputation):

    re_consonants = re.compile(r'[bcdfghjklmnpqrstvwxz]', re.IGNORECASE)

    def run(self):
        vowels = re.sub(self.re_consonants, '_', self.full_name)
        digits = utils.digitize(vowels)

        self._result = utils.simplify(digits)
        self._example = utils.examplify(vowels, digits, self._result)
