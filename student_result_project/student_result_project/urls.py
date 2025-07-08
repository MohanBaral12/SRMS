"""
URL configuration for student_result_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import*

urlpatterns = [
    path('admin/', admin.site.urls),                  # Django admin
    path('', index, name='index'),              # Main landing page (for {% url 'index' %} in templates)
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('home/', home, name='home'),           # Home/info page
    path('contact/', contact, name='contact'),  # Contact page
    path('fetch-data/', fetch_data, name='fetch_data'), # Contact form POST handler
]
