from django import forms
from django.core.validators import validate_email
from django.core.validators import ValidationError


def validate_not_gmail(value):
    if value.find('@gmail')!=-1:
        raise ValidationError(
            "Gmail is not allowed",
            params={'value':value},
        )


class LoginForm(forms.Form):
    email=forms.EmailField(max_length=18,min_length=8,validators=[validate_email])
    password=forms.CharField(max_length=18,min_length=8,widget=forms.PasswordInput)


 