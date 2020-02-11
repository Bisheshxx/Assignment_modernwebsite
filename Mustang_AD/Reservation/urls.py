from django.urls import path

from Reservation import views

urlpatterns = [
    path('', views.Reservations, name='Reservation'),

]