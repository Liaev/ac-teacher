# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from marshmallow import ValidationError


def validate_data(serializer):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                data = serializer().load(json.loads(args[1].body))
                kwargs['data'] = data
                return func(*args, **kwargs)
            except ValidationError as err:
                return JsonResponse(
                    status=400,
                    data=err.messages
                )

        return wrapper
    return decorator
