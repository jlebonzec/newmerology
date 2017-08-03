import json

from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic.detail import DetailView

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
        person = models.Person.objects.all().get_or_create(
            given_names=inst.given_names,
            last_name=inst.last_name,
            birth=inst.birth
        )
        return redirect(reverse('calc:person', kwargs={'pk': person.pk}))

    return HttpResponse(render(
        request, 'calculator/index.djt', context={'person_form': person_form}
    ))


class PersonDetailView(DetailView):

    model = models.Person


# -- User hidden views (XHR)
def update_content_model(request, pk, model):
    if request.POST:
        explanation = request.POST.get('explanation')
        if explanation is not None:
            explanation = explanation.strip()
            model.objects.all().filter(pk=pk).update(explanation=explanation)

            resp = {
                'status': 'success',
                'data': explanation
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
