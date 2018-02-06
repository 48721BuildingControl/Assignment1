from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('HVAC.html', views.HVAC),
    path('about.html', views.about),
    path('service.html', views.service),
    path('tbd.html', views.tbd),
]