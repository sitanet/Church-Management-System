from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('display_all_member/', views.display_all_member, name='display_all_member'),
    path('display_comment/', views.display_comment, name='display_comment'),
    path('new_comment/', views.new_comment, name='new_comment'),
    
 
    
]