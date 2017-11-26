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

""" LifePath pattern number.

It consists in the sum of the birth numbers
"""
from django_translate.services import tranz

from calculator.computations import utils
from calculator.config import POWERS


class Computation(utils.AbstractBaseComputation):

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
        formatted_birth = "%s + %s + %s" % (tranz("g.year"), tranz("g.month"), tranz("g.day"))
        formatted_sum = "%04d + %02d + %02d" % (year, month, day)
        self._example = utils.examplify(formatted_birth, formatted_sum, self._result)
