from django.urls import path
from . import views



app_name='quiz'
urlpatterns=[
    path('members/',views.members,name='members'),
    path('members/register/',views.register,name='register'),
    path('members/register/registerdb/',views.registerdb,name='registerdb'),
    path('members/login/',views.login,name='login'),
    path('members/login/logindb/',views.logindb,name='logindb'),
    
    path('login',views.registerdb,name='registerdb'),
    path('login/', views.login, name='login'),
    
    path('dashboard/',views.dashboard,name='dashboard'),
    path('science/',views.science,name='science'),
    path('sub_ch/', views.sub_ch, name='sub_ch'),
    path('record/', views.record, name='record'),

   
   

]


