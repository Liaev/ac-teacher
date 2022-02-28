# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


class LoginSerializer(Schema):
    username = fields.Str()
    password = fields.Str()


class GradeSerializer(Schema):

    student_id = fields.UUID()
    score = fields.Decimal(places=2)


