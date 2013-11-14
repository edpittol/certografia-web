from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = patterns('',
    url(r'^$', views.home),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
