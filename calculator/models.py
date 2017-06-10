from django.db import models
from django.dispatch import receiver

import datetime
import json

# TODO: names and __str__ / __repr__

""" Models and Signals used during the calculation

Meanings:
- User: the physical person
- Number: the name of the computable digit (i.e. "Life path", "Master number", etc)
- Template: generic explanation of a value obtained by a Number computation (see above)
- Result: Personalized explanation of a value obtained by a Number computation
"""


class User(models.Model):
    """ The user model. This model corresponds to the physical person asking for a study.
    """
    first_name = models.CharField(max_length=80, null=False, blank=False)
    middle_names = models.CharField(max_length=160, default='[]', null=False, blank=True)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    birth = models.DateField(null=False, blank=False)

    class Meta:
        unique_together = ('first_name', 'middle_names', 'last_name', 'birth')
        index_together = ('first_name', 'middle_names', 'last_name', 'birth')

    def __repr__(self):
        names = [self.first_name]
        names += self.middle_names
        names = [name.title() for name in names]
        return "<User: %s %s (%s)>" % (', '.join(names), self.last_name.upper(), self.birth)

    def __str__(self):
        return "%s %s" % (self.first_name.title(), self.last_name.upper())


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
    position = models.SmallIntegerField(default=0)
    computation_method = models.CharField(max_length=80, null=True)

    # TODO: Create methods to handle position while inserting or swapping

    class Meta:
        ordering = ['position', 'code']

    def __repr__(self):
        return "<Number: %s>" % self.code

    def __str__(self):
        return self.name


class AbstractContentModel(models.Model):
    """ Abstract model representing an explanation of the result of a computable Number

    example: The person obtained 3 to a number computation:
        value = 3
        explanation = "That's a great result!"
    """
    value = models.SmallIntegerField(null=False)
    explanation = models.TextField(default='', null=False, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.explanation


class Template(AbstractContentModel):
    """ Generic explanation of a value obtained by a computation
    """
    number = models.ForeignKey(Number, on_delete=models.CASCADE,
                               related_name='templates', related_query_name='template')

    class Meta:
        unique_together = ('number', 'value')
        index_together = ('number', 'value')

    def __repr__(self):
        return "<Template: [%s, %s]>" % (self.number.code, self.value)


class Result(AbstractContentModel):
    """ Personalized explanation of a value obtained by a computation.

    It's linked to a user, and is versioned through dates
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='results', related_query_name='result')
    number = models.ForeignKey(Number, on_delete=models.CASCADE,
                               related_name='results', related_query_name='result')
    date = models.DateTimeField(null=False, blank=False)  # This should never be directly edited

    __original_explanation = None

    def __init__(self, *args, **kwargs):
        super(Result, self).__init__(*args, **kwargs)
        self.__original_explanation = self.explanation

    class Meta:
        unique_together = ('user', 'number', 'value', 'date')  # include date to keep history
        index_together = ('user', 'number', 'value', 'date')  # include date to keep history

    def __repr__(self):
        return "<Result: %s - [%s, %s]>" % (self.user, self.number.code, self.value)

    def save(self, *args, **kwargs):
        """ Override the save method to properly handle versions
        """
        if not self.date or self.__original_explanation is not self.explanation:
            # Actually update the record
            now = datetime.datetime.now()
            super(Result, self).save(*args, **kwargs)
            self.__original_explanation = self.explanation
            self.date = now


# ------------- #
# -- Signals -- #

@receiver(models.signals.post_init, sender=User)
@receiver(models.signals.post_save, sender=User)
def serialize_user(sender, **kwargs):
    """ Transform the middle names list into json
    """
    obj = kwargs['instance']
    try:
        obj.middle_names = json.loads(obj.middle_names)
    except TypeError:
        # Probably first initialization, ignore
        pass


@receiver(models.signals.pre_save, sender=User)
def deserialize_user(sender, **kwargs):
    """ Transform the middle names json into a list
    """
    obj = kwargs['instance']
    obj.middle_names = json.dumps(obj.middle_names)
