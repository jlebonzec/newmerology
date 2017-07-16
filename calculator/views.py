from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic.detail import DetailView
from django.db.utils import IntegrityError

from . import forms
from . import models


def calculation(request):
    person_form = forms.PersonForm()

    if request.method == 'POST':
        person_form = forms.PersonForm(request.POST)
        if person_form.is_valid():
            person = person_form.instance
            try:
                person = person_form.save()
            except IntegrityError:
                person = models.Person.objects.all().filter(
                    given_names=person.given_names,
                    last_name=person.last_name, birth=person.birth)[0]
            return redirect(reverse('calc:person', kwargs={'pk': person.pk}))

    return HttpResponse(render(
        request, 'calculator/index.djt', context={'person_form': person_form}
    ))


class PersonDetailView(DetailView):

    model = models.Person
