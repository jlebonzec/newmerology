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

import json

from html import unescape
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.utils.html import escape
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from django_translate.services import tranz

from . import forms
from . import models


# -- User accessible views

def calculation(request):
    """ Propose a form to realize an analysis of someone.

    If the form is valid, the person is saved to DB and their numbers are
    computed.
    """
    person_form = forms.PersonForm(request.POST or None)

    if request.method == 'POST' and person_form.is_valid():
        inst = person_form.instance

        # Get or create from DB
        person, created = models.Person.objects.all().get_or_create(
            given_names=inst.given_names,
            last_name=inst.last_name,
            birth=inst.birth
        )
        return redirect(reverse('calc:person', kwargs={'pk': person.pk}))

    return HttpResponse(render(
        request, 'calculator/index.djt', context={'person_form': person_form}
    ))


class PersonListView(ListView):

    model = models.Person
    template_name = "calculator/person_list.djt"
    title = tranz("page.titles.person_list")


class PersonDetailView(DetailView):

    model = models.Person
    template_name = "calculator/person.djt"
    title = tranz("page.titles.person_detail")


class PersonDeleteView(DeleteView):

    model = models.Person
    template_name = "calculator/person_delete.djt"
    title = tranz("page.titles.person_delete")
    success_url = reverse_lazy("calc:people")


# -- User hidden views (XHR)
def update_content_model(request, pk, model):
    if request.POST:
        explanation_md = request.POST.get('explanation')
        if explanation_md is not None:
            explanation_md = escape(unescape(explanation_md.strip()))
            instance = model.objects.all().filter(pk=pk).first()
            instance.explanation_md = explanation_md
            instance.save()

            resp = {
                'status': 'success',
                'data': {
                    'markdown': instance.explanation_md,
                    'html': instance.explanation
                }
            }
            return HttpResponse(json.dumps(resp),
                                content_type="application/json",
                                status=200)

    resp = {
        'status': 'error'
    }
    return HttpResponse(json.dumps(resp),
                        content_type="application/json",
                        status=500)


def update_template(request, pk):
    return update_content_model(request, pk, models.Template)


def update_result(request, pk):
    return update_content_model(request, pk, models.Result)
