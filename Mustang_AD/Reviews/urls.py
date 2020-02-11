from django.urls import path

from Reviews import views

urlpatterns = [
    path('', views.bikereviews, name='Reviews'),

]