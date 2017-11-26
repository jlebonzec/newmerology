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

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /calculator/
    url(r'^$', views.calculation, name='home'),

    # ex: /calculator/person/
    url('^person/$', views.PersonListView.as_view(), name="people"),

    # ex: /calculator/person/4
    url(r'^person/(?P<pk>\d+)/$', views.PersonDetailView.as_view(), name='person'),

    # ex: /calculator/person/
    url(r'^person/delete/(?P<pk>\d+)/$', views.PersonDeleteView.as_view(), name='person_delete'),

    # ex: /calculator/update/template/2
    url(r'^update/template/(?P<pk>\d+)/$', views.update_template, name='update_template'),

    # ex: /calculator/update/result/6
    url(r'^update/result/(?P<pk>\d+)/$', views.update_result, name='update_result'),
]
