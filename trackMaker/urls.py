from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [             
    path('home1',views.home1,name="home1"),     
    path('registration1/',views.registration1,name="registration1"),    # View of Registration Page
    path('login1',views.login1,name="login1"),                         # View of Login Page
    path('logged_home',views.logged_home,name="logged_home"),       # View of Home Page after logging in
    path('track_home',views.track_home,name="track_home"),
    
    path('songPublish',views.songPublish,name="songPublish"),
    path('makeRequest',views.makeRequest,name="makeRequest"),
    path('viewRequest',views.viewRequest,name="viewRequest"),
    path('listen',views.listen,name="listen"),
    path('logout_track/', views.logout_track, name='logout_track'),
    
]
