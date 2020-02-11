from django.urls import path
from login import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard)
]
