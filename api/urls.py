# -*- coding: utf-8 -*-
from django.urls import path, include

from api.views import CourseApiView, GradeApiView, ProjectApiView, LoginApiView


urlpatterns = [
    path('oauth/token', LoginApiView.as_view(), name='oauth'),
    path('courses/', CourseApiView.as_view(), name='courses'),
    path('courses/<str:course_id>/', ProjectApiView.as_view(), name='projects'),
    path('projects/<str:project_id>/', GradeApiView.as_view(), name='project_grades'),

]