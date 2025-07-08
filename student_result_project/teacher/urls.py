from django.contrib import admin
from django.urls import path, include
from teacher.views import *

urlpatterns = [
    path('teacher-home/', teacher_home, name='teacher_home'),
    path('', login, name='login'),
    path('check-login/', check_login, name='t_check_login'),
    path('add-marks-form/', add_marks_form, name='add_marks_form'),
    path('add-marks/', set_marks, name='set_marks'),
    path('set-assignment/', set_assignment, name='set_assignment'),
    path('add-assignment/', add_assignment, name='add_assignment'),
    path('subject/', show_subject_name  , name='show_subject_name'),    
    path('student/', student  , name='student_portal'),
    path('set_student/', set_student  , name='set_student'),
    path('contact-form/', contact_form  , name='contact_form'),
    path('contact-data/', contact_data  , name='contact_data'),
    
]

