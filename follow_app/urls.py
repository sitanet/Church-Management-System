from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    path('home/', views.home, name='home'),
 
    
]