from django.db import models

# Create your models here.

# TODO: names and __str__ / __repr__


class User(models.Model):
    first_name = models.CharField(max_length=80, null=False, blank=False)
    middle_name = models.CharField(max_length=160, default='', null=False, blank=True)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    birth = models.DateField(null=False, blank=False)

    class Meta:
        unique_together = ('first_name', 'middle_name', 'last_name', 'birth')
        index_together = ('first_name', 'middle_name', 'last_name', 'birth')


# TODO: change class name
class Number(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(default='', null=False, blank=True)


class AbstractContentModel(models.Model):
    value = models.SmallIntegerField(max_length=2, null=False)
    explanation = models.TextField(default='', null=False, blank=True)

    class Meta:
        abstract = True


class Template(AbstractContentModel):
    # TODO: rename this field below
    code = models.ForeignKey(Number, on_delete=models.CASCADE,
                             related_name='templates', related_query_name='template')

    class Meta:
        unique_together = ('code', 'value')
        index_together = ('code', 'value')


class Result(AbstractContentModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='results', related_query_name='result')
    code = models.ForeignKey(Number, on_delete=models.CASCADE,
                             related_name='results', related_query_name='result')
    date = models.DateField(null=False, blank=False)

    class Meta:
        unique_together = ('user', 'code', 'value', 'date')  # include date to keep history
        index_together = ('user', 'code', 'value', 'date')  # include date to keep history
