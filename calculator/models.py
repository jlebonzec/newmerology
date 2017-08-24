from django.db import models

from calculator.utils import markdownify
from importlib import import_module

from calculator.config import COMPUTATION_METHODS_PATH, GIVEN_NAMES_SEPARATOR

# TODO: names and __str__ / __repr__

""" Models and Signals used during the calculation

Meanings:
- Person: the physical person
- Number: the name of the computable digit (i.e. "Life path", "Master number", etc)
- Template: generic explanation of a value obtained by a Number computation (see above)
- Result: Personalized explanation of a value obtained by a Number computation
"""


class Person(models.Model):
    """ The person model. This model corresponds to the physical person asking for a study.
    """
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
        (None, 'Gender'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    given_names = models.CharField(max_length=80, null=False, blank=False,
                                   help_text="All, space-separated")
    last_name = models.CharField(max_length=50, null=False, blank=False)
    birth = models.DateField(null=False, blank=False, help_text="YYYY-MM-DD")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)

    class Meta:
        unique_together = ('given_names', 'last_name', 'birth')
        index_together = ('given_names', 'last_name', 'birth')

    @property
    def first_name(self):
        return self.given_names.split(GIVEN_NAMES_SEPARATOR)[0].title()

    @property
    def middle_names(self):
        return [n.title() for n in self.given_names.split(GIVEN_NAMES_SEPARATOR)[1:]]

    @property
    def full_name(self):
        return " ".join((self.last_name, self.given_names))

    @property
    def numbers(self):
        if self._numbers is None:
            self.refresh_numbers()
        return self._numbers

    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self._numbers = None

    def __repr__(self):
        names = self.given_names.split(' ')
        names = [name.title() for name in names]
        return "<Person: %s %s (%s)>" % (', '.join(names), self.last_name.upper(), self.birth)

    def __str__(self):
        return "%s %s" % (self.first_name.title(), self.last_name.upper())

    def refresh_numbers(self):
        computations = Number.objects.filter(position__gte=0)
        for comp in computations:
            comp.person = self
        self._numbers = computations


class Number(models.Model):
    """ The Number model. It contains shortened names and descriptions corresponding to
    computable Numbers.

    example: Life Path pattern Number is a computable Number

    The position indicates the order for display.
        - -1 hides the element
        - Order is ascending
        - If two elements have the same position (it should not happen), the code is then used

    The computation method is a string corresponding to an existing python method.
    It will be imported when computing elements.
    """
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(default='', null=False, blank=True)
    position = models.SmallIntegerField(default=0)  # -1 means disabled
    computation_method = models.CharField(max_length=80, null=True)

    # TODO: Create methods to handle position while inserting or swapping
    # TODO: How to handle grid and numerological table?

    class Meta:
        ordering = ['position', 'code']

    def __init__(self, *args, **kwargs):
        super(Number, self).__init__(*args, **kwargs)
        self._template = None
        self._result = None
        self._person = None
        self.computation = None

    def __repr__(self):
        return "<Number: %s>" % self.code

    def __str__(self):
        return self.name

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        if not self._person and value:
            self._person = value

            if self.computation_method:
                self.computation = import_module(
                    COMPUTATION_METHODS_PATH + self.computation_method
                ).Computation(self._person)

    @property
    def template(self):
        self.refresh_explanations()
        return self._template

    @property
    def result(self):
        self.refresh_explanations()
        return self._result

    def refresh_explanations(self, force=False):
        """ Refresh the explanation. Will only work if self.computations and self.person are set.
        
        :param force: If we should force the refresh of the explanations (even if already computed)
        :type force: bool
        """
        if not self.computation:
            return
        if self.person and any((force, self._template is None, self._result is None)):
            self._result = self.results.filter(person=self.person, value=self.computation.result).first()
            if self._result is None:
                self._result = Result(number=self,
                                      person=self.person,
                                      value=self.computation.result)
                self._result.save()

            self._template = self.templates.filter(value=self.computation.result).first()
            if self._template is None:
                self._template = Template(number=self, value=self.computation.result)
                self._template.save()


class AbstractContentModel(models.Model):
    """ Abstract model representing an explanation of the result of a computable Number

    example: The person obtained 3 to a number computation:
        value = 3
        explanation = "That's a great result!"
    """
    value = models.SmallIntegerField(null=False)
    explanation_md = models.TextField(default='', null=False, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.explanation_md

    @property
    def explanation(self):
        return markdownify(self.explanation_md)


class Template(AbstractContentModel):
    """ Generic explanation of a value obtained by a computation
    """
    number = models.ForeignKey(Number, on_delete=models.CASCADE,
                               related_name='templates', related_query_name='template')

    class Meta:
        unique_together = ('number', 'value')

    def __repr__(self):
        return "<Template: [%s, %s]>" % (self.number.code, self.value)


class Result(AbstractContentModel):
    """ Personalized explanation of a value obtained by a computation.

    It's linked to a person, and is versioned through dates
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE,
                               related_name='results', related_query_name='result')
    number = models.ForeignKey(Number, on_delete=models.CASCADE,
                               related_name='results', related_query_name='result')
    # TODO: Add date for history analysis

    class Meta:
        ordering = ['person', 'number', 'value']

    def __repr__(self):
        return "<Result: %s - [%s, %s]>" % (self.person, self.number.code, self.value)
