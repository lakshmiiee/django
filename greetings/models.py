from django.db import models
from django.core.validators import validate_email

# Create your models here.

class Login(models.Model):
    email=models.CharField(max_length=100,validators=[validate_email])
    password=models.CharField(max_length=20)


class Customer(models.Model):
    email = models.CharField(max_length=100,)
    password = models.CharField(max_length=50)