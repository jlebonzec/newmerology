from django import template
from django_translate.services import tranz


register = template.Library()


@register.inclusion_tag('helpers/weekdays_full.djt')
def weekdays_full():
    """ Display the full name of days for JS, translated
    """
    prefix = 'g.days.full.'
    days = []
    for i in range(1, 8):
        day_name = prefix + str(i)
        days.append(tranz(day_name))
    return {'days': days}
