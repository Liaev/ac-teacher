# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class GradeForm(forms.Form):
    score = forms.DecimalField(max_digits=3, max_value=10, min_value=0)
