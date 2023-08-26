from django.urls import path
from . import views



urlpatterns = [
    path('registeruser/', views.registeruser, name='registeruser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    # path('login/', views.login, name='login'),
 
    
]