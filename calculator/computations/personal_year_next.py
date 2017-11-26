#   This file is part of Newmerology.
#
#   Newmerology is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Newmerology is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with Newmerology.  If not, see <https://www.gnu.org/licenses/agpl.html>.

""" Next Personal Year.

It consists in the sum of the birth numbers, but replacing the birth year with the current year
"""
from django_translate.services import tranz

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        year, month, day = self.today.year + 1, self.birth.month, self.birth.day
        num = utils.simplify(year + month + day, keep_power=False)
        self._result = num

        # Compute the example
        formatted_birth = "%s + %s + %s" % (tranz("g.u_year"), tranz("g.month"), tranz("g.day"))
        formatted_sum = "%04d + %02d + %02d" % (year, month, day)
        self._example = utils.examplify(formatted_birth, formatted_sum, self._result)
