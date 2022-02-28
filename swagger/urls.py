# -*- coding: utf-8 -*-

from django.urls import path
from swagger.views import SwaggerView

urlpatterns = [
    path('', SwaggerView.as_view(), name='swagger'),
]
