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

from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from material import Layout, Row
from . import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['given_names', 'last_name', 'birth', 'gender']

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique."
            }
        }

    layout = Layout(
        Row('given_names', 'last_name'),
        Row('birth', 'gender')
    )
