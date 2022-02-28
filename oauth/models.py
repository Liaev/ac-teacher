# -*- coding: utf-8 -*-
import uuid
from datetime import datetime, timedelta

from django.db import models

from main.models import Teacher


def expire_default():
    return datetime.now() + timedelta(hours=24)


class Token(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    expire = models.DateTimeField(default=expire_default)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)