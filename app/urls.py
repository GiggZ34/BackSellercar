from django.urls import path
from . import views

urlpatterns = [
    path('getAllCars', views.getAllCars, name='getAllCars'),
    path('insertCar', views.insertCar, name='insertCar'),
]
