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

from django import template

from calculator.computations.time_computation import AbstractTimeComputation
from calculator.config import TIMELINE_MAXIMUM


register = template.Library()


@register.inclusion_tag('helpers/display_timeline.djt')
def display_timeline(timeline):
    """ Display a timeline.

    If one period starts after the maximum, we normalize the values

    :param timeline: The timeline object
    :type timeline: AbstractTimeComputation
    """
    periods = timeline.periods

    for i, period in enumerate(periods):
        last = i+1 >= len(periods)

        if not last:
            next_period = periods[i+1]
            size = next_period['start'] - period['start']
        else:
            size = TIMELINE_MAXIMUM - period['start']

        period.update({
            'size': str(size) + "%",
        })
    return {'periods': timeline.periods, 'period_id': timeline.period_id, 'now': timeline.age}
