from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    path('register_member/', views.register_member, name='register_member'),
    path('display_all_member/', views.display_all_member, name='display_all_member'),
    path('display_comment/', views.display_comment, name='display_comment'),
    path('all_comment/', views.all_comment, name='all_comment'),
    path('new_comment/<int:id>/', views.new_comment, name='new_comment'),
    path('member_detail/<int:id>/', views.member_detail, name='member_detail'),
    path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
    path('add_coordinator/', views.add_coordinator, name='add_coordinator'),
    
   
    
    


    
 
    
]