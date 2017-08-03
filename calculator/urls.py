from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /calculator/
    url(r'^$', views.calculation, name='home'),

    # ex: /calculator/person/4
    url(r'^person/(?P<pk>\d+)/$',
        views.PersonDetailView.as_view(template_name="calculator/person.djt"),
        name='person'),

    # ex: /calculator/update/template/2
    url(r'^update/template/(?P<pk>\d+)/$',
        views.update_template,
        name='update_template'),

    # ex: /calculator/update/result/6
    url(r'^update/result/(?P<pk>\d+)/$',
        views.update_result,
        name='update_result'),
]
