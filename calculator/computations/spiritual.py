""" Spiritual number.

It consists in the mapped sum of the vowels of the full name
"""

from calculator.computations import utils

import re


class Computation(utils.AbstractComputation):

    re_consonants = re.compile(r'[bcdfghjklmnpqrstvwxz]', re.IGNORECASE)

    def run(self):
        vowels = self.re_consonants.sub(self.full_name, '_')
        digits = utils.string_to_digits(vowels)

        self._result = utils.simplify(digits)
        self._example = utils.conversion_to_example(vowels, digits, self._result)
