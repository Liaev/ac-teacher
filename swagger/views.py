# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import View


class SwaggerView(View):

    template_name = 'swagger.html'

    def get(self, request):
        return render(request, self.template_name)
