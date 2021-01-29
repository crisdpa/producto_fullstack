"""
Main URL Configuration
"""
from django.conf.urls import url, include
from opianalytics.apps.location import views
from django.conf import settings
from django.conf.urls.static import serve


urlpatterns = [
    url(r'^$', views.home, name="home"),
    # url(r'^api/', include('opianalytics.api.urls')),
]