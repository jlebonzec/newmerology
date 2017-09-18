from django.conf.urls import include, url
from calculator import urls as calc_urls

urlpatterns = [
    url(r'', include(calc_urls, namespace='calc')),
]
