from django.urls import path
from . import views  

urlpatterns = [
    #Login
    path('login/<email>/<password>', views.login, name='login'),

    #UserType
    path('get-user-types/', views.get_usertype, name='get-user-types'),

    #Activity
    path('get-activity-senior-citizen/', views.get_activity_senior_citizen, name='get-activity-senior-citizen'),
    path('get-activity-child/', views.get_activity_child, name='get-activity-child'),
    path('get-activity-pet/', views.get_activity_pet, name='get-activity-pet'),


    #User details
    path('user-details/<int:id>/', views.user_details, name='user-details'),
    path('add-user/', views.add_user, name='add-user'),
    path('get-all-users/', views.get_all_users, name='get-all-users'),

    #Senior citizen details
    path('get-all-senior-citizens/', views.get_all_senior_citizens, name='get-all-senior-citizens'),
    path('senior-citizen-details/<int:id>/', views.senior_citizen_details, name='senior-citizen-details'),
    path('add-senior-citizen/', views.add_senior_citizen, name='add-new-senior-citizen'),
    path('get-my-senior-citizen/<int:id>/', views.get_my_senior_citizen, name='get_my_senior_citizen'),


    #Child details
    path('get-all-children/', views.get_all_children, name='get-all-children'),
    path('child-details/<int:id>/', views.child_details, name='child-details'),
    path('add-child/', views.add_child, name='add-new-child'),
    path('get-my-childs/<int:id>/', views.get_my_childs, name='get_my_childs'),


    #Pet details
    path('get-all-pets/', views.get_all_pets, name='get-all-pets'),
    path('pet-details/<int:id>/', views.pet_details, name='pet-details'),
    path('add-pet/', views.add_pet, name='add-new-pet'),
    path('get-my-pets/<int:id>/', views.get_my_pets, name='get_my_pets'),


    #TOPY Station
    path('get-topystations/', views.get_topystations, name='get-all-topystations'),

    #Match details
    path('get-matchs-incoming/<int:id>', views.get_matchs_incoming, name='get-matchs-incoming'),
    path('get-matchs-outgoing/<int:id>', views.get_matchs_outgoing, name='get-matchs-outgoing'),
    path('get-matchs-past/<int:id>', views.get_matchs_past, name='get-matchs-past'),
    path('match-details/<int:id>/', views.match_details, name='match-details'),
    path('add-match/', views.add_match, name='add-new-match'),
    path('get-all-matchs/', views.get_all_matchs, name='get-all-matchs'),

    # path('get-topystation/', views.get_topystation, name='get-all-topystations'),
    # path('match-details/', views.match_details, name='match-details'),


    #Get Recommendation
    path('get-recommendation-for-senior-citizen-activity/<int:id>/', views.get_recommendation_for_senior_citizen_activity, name='get-recommendation-for-senior-citizen-activity'),
    path('get-recommendation-for-child-activity/<int:id>/', views.get_recommendation_for_child_activity, name='get-recommendation-for-child-activity'),
    path('get-recommendation-for-pet-activity/<int:id>/', views.get_recommendation_for_pet_activity, name='get-recommendation-for-pet-activity'),
    path('get-recommendation-for-child/<int:id>/', views.get_recommendation_for_child, name='get-recommendation-for-child'),

    # path('get-recommendation-for-senior-citizen-location/<int:id>/', views.get_recommendation_for_senior_citizen_location, name='get-recommendation-for-senior-citizen-location'),
    path('get-recommendation-for-child-location/<int:id>/', views.get_recommendation_for_child_location, name='get-recommendation-for-child-location'),
    # path('get-recommendation-for-pet-location/<int:id>/', views.get_recommendation_for_pet_location, name='get-recommendation-for-pet-location'),
    path('get-recommendation-for-senior/<int:id>/', views.get_recommendation_for_senior, name='get-recommendation-for-senior'),
    path('', views.getData),
    # path('add',views.addUser),
    # path('get-all-usertype',views.get_all_usertype)
    # path('get-usertype-id', views.get_usertype_id)
 ]

