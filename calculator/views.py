from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def calculation(request):
    template = loader.get_template('calculator/index.html')
    return HttpResponse(template.render(context={}, request=request))
