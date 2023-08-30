from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
  
    path('register_member/', views.register_member, name='register_member'),
    path('display_all_member/', views.display_all_member, name='display_all_member'),
    path('display_comment/', views.display_comment, name='display_comment'),
    path('new_comment/', views.new_comment, name='new_comment'),
    
 
    
]