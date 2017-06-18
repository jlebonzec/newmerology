from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse

from . import forms
from . import models
from . import utils

import datetime


def calculation(request):
    if request.method == 'POST':
        person_form = forms.PersonForm(request.POST)
        if person_form.is_valid():
            return redirect(reverse('calc:results'))
        else:
            return HttpResponse(render(
                request, 'calculator/index.djt', context={'person_form': person_form}
            ))
    else:
        person_form = forms.PersonForm()

        return HttpResponse(render(
            request, 'calculator/index.djt', context={'person_form': person_form}
        ))


def results(request):
    context = {
        'person': {
            'id': 1,
            'given_names': 'Jonathan Jean MAURICE',
            'first_name': 'Jonathan',
            'middle_names': ['Jean', 'Maurice'],
            'last_name': 'Le Bonzec',
            'birth': datetime.date(1994, 1, 6),
            'full_name': 'LE BONZEC Jonathan, Jean, Maurice, 1994-01-06',

            'numbers': [
                {
                    'code': 'annee_universelle',
                    'position': 0,
                    'name': 'Année universelle',
                    'description': "La numérologie de l'année ; la même pour tout le monde",
                    'value': 1,
                    'example': [
                        '2017 = 1'
                    ],
                    'template': {  # Create if not existent
                        'id': 3,
                        'value': 1,
                        'explanation': 'Année plutôt puissante'
                    },
                    'result': {  # Create if it doesn't exist
                        'id': 17,
                        'value': 1,
                        'explanation': '',
                    }
                },
                {
                    'code': 'chemin',
                    'position': 0,
                    'name': 'Chemin de vie',
                    'description': 'Le nombre qui vous guidera toute votre vie',
                    'value': 3,
                    'example': [
                        '1994-01-06',
                        '1994+01+06 = 3'
                    ],
                    'template': {  # Create if not existent
                        'id': 12,
                        'value': 3,
                        'explanation': 'Texte par défault pour le chemin de vie #3'
                    },
                    'result': {  # Create if it doesn't exist
                        'id': 17,
                        'value': 3,
                        'explanation': 'Le chemin de vie 3 est un chemin de vie artistique',
                    }
                }
            ]
        }
    }
    return HttpResponse(render(request=request,
                               template_name='calculator/results.djt',
                               context=context))
