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

""" Active number.

It consists in the mapped sum of the given names
"""

from calculator.computations import utils


class Computation(utils.AbstractBaseComputation):

    def run(self):
        digits = utils.digitize(self.given_names)

        self._result = utils.simplify(digits)
        self._example = utils.examplify(self.given_names, digits, self._result)
