from django.conf.urls import include, url
from django.contrib import admin
from calculator import urls as calc_urls

from markdownx import urls as markdownx

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^calculator/', include(calc_urls, namespace='calc')),
    url(r'^markdownx/', include(markdownx))
]
