from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('registration/', views.registration, name = 'registration'),
    path('home', views.home, name = 'home'),
    path('event', views.event, name = 'event'),
    path('notify', views.notify, name = 'notify'),
    path('logout/', views.logout_view, name='logout'),
]
