from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    
    #/music/<id>/
    path('<id>/', views.search, name='search')
]
