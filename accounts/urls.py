from django.urls import path
from . import views



urlpatterns = [
    path('team_dashboard/', views.team_dashboard, name='team_dashboard'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('coor_dashboard/', views.coor_dashboard, name='coor_dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('change_password/', views.change_password, name='change_password'),
 
    
]