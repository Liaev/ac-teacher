# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Union

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpRequest

from oauth.exceptions import InvalidToken
from oauth.models import Token


def authenticate_request(request: HttpRequest) -> Token:
    auth = request.META.get('HTTP_AUTHORIZATION')
    try:
        if auth:
            token = Token.objects.get(token=auth.split(" ")[1],
                                      expire__gte=datetime.now())
            return token
        else:
            raise InvalidToken
    except (ObjectDoesNotExist, ValidationError, TypeError, ValueError) as e:
        print('\033[92m{}\033[0m'.format(e))
        raise InvalidToken
    raise InvalidToken


