# -*- coding: utf-8 -*-
from django.http import HttpRequest, JsonResponse

from main.models import Teacher
from oauth.autenticate import authenticate_request
from oauth.exceptions import InvalidToken


def get_teacher(request: HttpRequest) -> Teacher:
    token = authenticate_request(request)
    return token.teacher


def teacher_api_authenticated(func):
    def wrapped(*args, **kwargs):
        try:
            kwargs['teacher'] = get_teacher(args[1]) #args[1] request object
        except InvalidToken:
            return JsonResponse(status=400, data={"error": "invalid token"})
        return func(*args, **kwargs)

    return wrapped
