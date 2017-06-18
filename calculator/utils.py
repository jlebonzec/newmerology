""" Compute various objects. Goal is to lighten the views file
"""

from . import models

# FIXME: figure out a way to ease edition of results and templates


def get_or_create_person(first_name, middle_names, last_name, birth):
    """ Get or create a user corresponding to the parameters

    :param first_name: The first name of the person
    :type first_name: str
    :param middle_names: The middle names of the person
    :type middle_names: list
    :param last_name: The last name of the person
    :type last_name: str
    :param birth: The birth date of the person
    :type birth: datetime.date

    :return: A user object matching the parameters.
    :rtype: models.Person
    """
    query_set = models.Person.objects.filter(first_name__iexact=first_name,
                                             last_name__iexact=last_name,
                                             birth__exact=birth)
    for middle_name in middle_names:
        query_set.filter(middle_names__icontains=middle_name)
    if query_set:
        return query_set[-1]
    else:
        return models.Person.objects.create(first_name=first_name, middle_names=middle_names,
                                            last_name=last_name, birth=birth)


def get_results(first_name, middle_names, last_name, birth):
    """ Compute results for a given person.

    :param first_name: The first name of the person
    :param middle_names: The list of middle names of the person
    :param last_name: The last name of the person
    :param birth: The date of birth of the person
    :return: A list of results, number by number
    """
    # Retrieve user.
    person = get_or_create_person(first_name, middle_names, last_name, birth)
    numbers_to_compute = models.Number.objects.filter(position__gte=0)
    results = []
    for number in numbers_to_compute:
        value = 7
        one_result = {
            'name': number.name,
            'description': number.description,
            'value': value,
            'explanation': get_person_explanation_for_number(person, number, value)
        }
        results.append(one_result)
    return results


def get_person_explanation_for_number(person, number, value):
    """ Get an explanation for a person, given a number and the value obtained

    Defaults to the template explanation if it cannot be found as is

    :param person: The person
    :type person: models.Person
    :param number: The number
    :param value: The Value
    :return: The explanation text
    """
    result = person.results.filter(number=number, value=value)
    if result:
        return result[-1].explanation  # Return the last explanation created
    else:
        template, created = models.Template.objects.get_or_create(number=number, value=value)
        return template.explanation
