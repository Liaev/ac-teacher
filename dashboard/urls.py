# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.urls import path

from dashboard.views import LoginView, DashboardView, CourseView, ProjectView, GradeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dashboard/<str:course_id>/', CourseView.as_view(), name='course_dashboard'),
    path('dashboard/<str:course_id>/<str:project_id>/',
         ProjectView.as_view(), name='project_dashboard'),
    path('dashboard/<str:course_id>/<str:project_id>/<str:grade_id>',
         GradeView.as_view(), name='grade_dashboard')
]
