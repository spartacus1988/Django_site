from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    path(r'', views.index, name = 'index')
]