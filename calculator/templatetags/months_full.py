from django import template
from django_translate.services import tranz


register = template.Library()


@register.inclusion_tag('helpers/months_full.djt')
def months_full():
    """ Display the full name of months for JS, translated
    """
    prefix = 'g.months.full.'
    months = []
    for i in range(1, 13):
        month_name = prefix + str(i)
        months.append(tranz(month_name))
    return {'months': months}
