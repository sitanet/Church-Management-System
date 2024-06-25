from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    # path('profile/', views.profile, name='profile'),
    path('register_member/', views.register_member, name='register_member'),
    path('display_all_member/', views.display_all_member, name='display_all_member'),
    path('display_kbn_business/', views.display_kbn_business, name='display_kbn_business'),
    path('display_kbn_car/', views.display_kbn_car, name='display_kbn_car'),
    
    path('member_detail_universal/<int:id>/', views.member_detail_universal, name='member_detail_universal'),
    path('member_male_detail/<int:id>/', views.member_male_detail, name='member_male_detail'),
    path('member_female_detail/<int:id>/', views.member_female_detail, name='member_female_detail'),

    path('family/<int:id>/', views.family_detail, name='family_detail'),
    path('families/<int:id>/delete/', views.delete_family, name='delete_family'),
    
    path('display_comment/', views.display_comment, name='display_comment'),
    path('all_comment/', views.all_comment, name='all_comment'),
    path('new_comment/<int:id>/', views.new_comment, name='new_comment'),
    path('member_detail/<int:id>/', views.member_detail, name='member_detail'),
    path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
    path('add_coordinator/', views.add_coordinator, name='add_coordinator'),
    path('network_not_available/', views.network_not_available, name='network_not_available'),
    path('admin_registration/', views.admin_registration, name='admin_registration'),


    path('members/', views.list_members, name='list_members'),
    path('list_members_student/', views.list_members_student, name='list_members_student'),
    path('create-student/<int:member_id>/', views.create_student, name='create_student'),
    path('student-success/', views.success_page, name='student_success'),

    path('create_nysc/<int:member_id>/', views.create_nysc, name='create_nysc'),
    path('success/', views.success, name='success'),
    path('nysc/', views.nysc, name='nysc'),


    path('create_child/<int:member_id>/', views.create_child, name='create_child'),
    path('child_success/', views.child_success, name='child_success'),
    path('list_members_child/', views.list_members_child, name='list_members_child'),
    path('children_detail/<int:id>/', views.children_detail, name='children_detail'),


    path('list_members_nysc/', views.list_members_nysc, name='list_members_nysc'),

    path('nysc_detail/<int:id>/', views.nysc_detail, name='nysc_detail'),
    


    # path('create_kbn/<int:member_id>/', views.create_kbn, name='create_kbn'),
    path('kbn_success/', views.kbn_success, name='kbn_success'),
    path('list_members_bus_kbn/', views.list_members_bus_kbn, name='list_members_bus_kbn'),
    path('list_members_car_kbn/', views.list_members_car_kbn, name='list_members_car_kbn'),

    
    path('create-family/<int:member_id>/', views.create_family, name='create_family'),
    path('search-wife/', views.search_wife, name='search_wife'),
    path('list_family/', views.list_family, name='list_family'),


    path('kbn_bus_car/', views.kbn_bus_car, name='kbn_bus_car'),

    path('create_career_profile/<int:member_id>/', views.create_career_profile, name='create_career_profile'),
    path('create_business_profile/<int:member_id>/', views.create_business_profile, name='create_business_profile'),

    path('career_list/', views.career_list, name='career_list'),
    path('<int:pk>/', views.career_detail, name='career_detail'),
    path('career/<int:pk>/delete/', views.career_delete, name='career_delete'),
    
    path('business_list/', views.business_list, name='business_list'),
    path('business_detail/<int:pk>/', views.business_detail, name='business_detail'),
    path('business/<int:pk>/delete/', views.business_delete, name='business_delete'),

    
    path('member_female/', views.member_female, name='member_female'),
    path('family/', views.family, name='family'),
    path('member_married/', views.member_married, name='member_married'),
    path('member_single/', views.member_single, name='member_single'),
    path('children/', views.children, name='children'),
    path('display_kbn_business_admin/', views.display_kbn_business_admin, name='display_kbn_business_admin'),
    path('display_kbn_car_admin/', views.display_kbn_car_admin, name='display_kbn_car_admin'),


    
    path('household_list/', views.household_list, name='household_list'),
    # path('households/add/', views.add_household, name='add_household'),
    # path('search-members/', views.search_members, name='search_members'),


    path('create_household/', views.create_household, name='create_household'),
    path('search_members/', views.search_members, name='search_members'),
    path('household/<int:household_id>/add/', views.add_household_member, name='add_household_member'),



    path('household/<int:household_id>/', views.household_detail, name='household_detail'),
    path('household/<int:household_id>/edit/<int:member_id>/', views.edit_household_member, name='edit_household_member'),
    path('household/<int:household_id>/delete/<int:member_id>/', views.delete_household_member, name='delete_household_member'),
    path('search_member_add/', views.search_member_add, name='search_member_add'),




    path('teenager_member_list/', views.teenager_member_list, name='teenager_member_list'),
    path('admin_teenager_list/', views.admin_teenager_list, name='admin_teenager_list'),
    path('teenagers/', views.teenager_list, name='teenager_list'),
    path('teenagers/add/<int:member_id>/', views.add_teenager, name='add_teenager'),
    path('teenagers/edit/<int:teenager_id>/', views.edit_teenager, name='edit_teenager'),
    path('teenagers/delete/<int:teenager_id>/', views.delete_teenager, name='delete_teenager'),
    path('teenagers/<int:teenager_id>/', views.teenager_detail, name='teenager_detail'),

]