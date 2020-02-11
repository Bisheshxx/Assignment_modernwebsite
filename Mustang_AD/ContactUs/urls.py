from django.urls import path

from ContactUs import views

urlpatterns = [
    path('', views.ContactUs, name='ContactUs'),

]