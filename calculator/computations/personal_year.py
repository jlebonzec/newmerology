""" Personal Year.

It consists in the sum of the birth numbers, but replacing the birth year with the current year
"""
from django_translate.services import tranz

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        year, month, day = self.today.year, self.birth.month, self.birth.day
        num = utils.simplify(year + month + day, keep_power=False)
        self._result = num

        # Compute the example
        formatted_birth = "%s + %s + %s" % (tranz("g.u_year"), tranz("g.month"), tranz("g.day"))
        formatted_sum = "%04d + %02d + %02d" % (year, month, day)
        self._example = utils.examplify(formatted_birth, formatted_sum, self._result)
