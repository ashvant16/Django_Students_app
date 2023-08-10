from django.urls import path
from . import views

urlpatterns = [
    path('',views.student,name="student"),
    path('teacher_login', views.teacher_login, name = 'teacher_login'),
    path('teacher_home', views.teacher_home, name = 'teacher_home'),
    path('delete-entry/', views.delete_entry, name='delete-entry'),
    path('ttform/', views.ttform, name='ttform'),
    path('remform/', views.remform, name='remform'),
    path('captcha/', views.captcha_image, name='captcha_image'),
    path('visualize_data/', views.visualize_data, name='visualize_data'),
    path('tlogout/', views.tlogout_view, name='tlogout'),
]
