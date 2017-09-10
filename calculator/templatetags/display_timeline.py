from copy import deepcopy

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
