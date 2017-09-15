from django.conf.urls import include, url
from calculator import urls as calc_urls

from markdownx import urls as markdownx

urlpatterns = [
    url(r'', include(calc_urls, namespace='calc')),
    url(r'^markdownx/', include(markdownx))
]
