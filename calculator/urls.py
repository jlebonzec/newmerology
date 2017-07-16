from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /calculator/
    url(r'^$', views.calculation, name='home'),
    # ex: /calculator/person
    url(r'^person/(?P<pk>\d+)/$',
        views.PersonDetailView.as_view(),
        name='person')
]
