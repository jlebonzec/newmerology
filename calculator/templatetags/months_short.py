from django import template
from django_translate.services import tranz


register = template.Library()


@register.inclusion_tag('helpers/months_short.djt')
def months_short():
    """ Display the short name of months for JS, translated
    """
    prefix = 'g.months.short.'
    months = []
    for i in range(1, 13):
        month_name = prefix + str(i)
        months.append(tranz(month_name))
    return {'months': months}
