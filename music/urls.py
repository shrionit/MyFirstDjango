from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index')
    
    # /music/<id>/
    path(r'^(?P<album_id>[0-9])$')
]
