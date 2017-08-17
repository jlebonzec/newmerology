""" Intimate number.

It consists in the mapped sum of the consonants of the full name
"""

from calculator.computations import utils

import re


class Computation(utils.AbstractComputation):

    re_vowels = re.compile(r'[aeiouy]', re.IGNORECASE)

    def run(self):
        consonants = self.re_vowels.sub(self.full_name, '_')
        digits = utils.string_to_digits(consonants)

        self._result = utils.simplify(digits)
        self._example = utils.conversion_to_example(consonants, digits, self._result)
