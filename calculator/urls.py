from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /calculator/
    url(r'^$', views.calculation, name='calculation'),
]
