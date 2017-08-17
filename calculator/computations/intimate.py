""" Intimate number.

It consists in the mapped sum of the consonants of the full name
"""

from calculator.computations import utils

import re


class Computation(utils.AbstractComputation):

    re_vowels = re.compile(r'[aeiouy]', re.IGNORECASE)

    def run(self):
        consonants = re.sub(self.re_vowels, '_', self.full_name)
        digits = utils.digitize(consonants)

        self._result = utils.simplify(digits)
        self._example = utils.examplify(consonants, digits, self._result)
