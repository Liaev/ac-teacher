# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect

from main.models import Teacher


def get_teacher(request: HttpResponse):
    """
    Get the teacher from the get request parameter
    :param request:
    :return:
    """
    teacher_id = request.GET.get('t')
    return Teacher.objects.get(id=teacher_id)


def teacher_authenticate(func):
    """
    Wrapped that get the teacher id from the get parameters and return the Teacher
    to the view
    :param func:
    :return:
    """
    def wrapped(*args, **kwargs):
        try:
            kwargs['teacher'] = get_teacher(args[1])
            return func(*args, **kwargs)
        except (ObjectDoesNotExist, ValidationError):
            return redirect("login")
    return wrapped