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

""" Seventh cell of the grid. See the AbstractGridComputation for how it's computed """

from calculator.computations.grid_computation import AbstractGridComputation


class Computation(AbstractGridComputation):

    def __init__(self, *args, **kwargs):
        super(Computation, self).__init__(*args, **kwargs)
        self.cell_id = 7
