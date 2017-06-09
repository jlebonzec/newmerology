from django.http import HttpResponse
from django.shortcuts import render


def calculation(request):
    return HttpResponse(render(request, 'calculator/index.jinja2', {}))


def results(request):
    return HttpResponse(render(request, 'calculator/results.jinja2', {'items': [1, 2, 3, 4]}))
