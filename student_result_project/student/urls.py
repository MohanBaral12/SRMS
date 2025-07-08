from django.contrib import admin
from django.urls import path, include
from .views import*

urlpatterns = [
    path('', stu_home, name="stu_home"),                  # Student home page
    path('check-login/', student_login, name="check_login"),
    path('student-home/', stu_home, name="stu_home"),
    path('profile/', stu_profile, name="stu_profile"),
   ]
