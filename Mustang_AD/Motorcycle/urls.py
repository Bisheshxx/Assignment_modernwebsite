from django.urls import path

from Motorcycle import views

urlpatterns = [
    path('', views.Motorcycle, name='Motorcycle'),

]