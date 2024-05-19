"""
URL configuration for exam_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apis.views.v1.school import *
from apis.views.v1.teacher import *
from apis.views.v1.student import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
    path('create_school/', SchoolCreateView.as_view(), name='school-create'),
    path('school_list/', SchoolListView.as_view(), name='school-list'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('classroom_list/', ClassRoomListView.as_view(), name='classroom-list'),
    path('create_classroom/', ClasRoomCreateView.as_view(), name='classroom-create'),
    path('classroom/<int:pk>/', ClassRoomDetailView.as_view(), name='classroom-detail'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher-list'),
    path('create_teacher/', TeacherCreateView.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('create_student/', StudentCreateView.as_view(), name='student-create'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
]
