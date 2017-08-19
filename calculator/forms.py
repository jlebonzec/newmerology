from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from material import Layout, Row
from . import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['given_names', 'last_name', 'birth']

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique."
            }
        }

    layout = Layout(
        Row('given_names', 'last_name'),
        Row('birth')
    )
