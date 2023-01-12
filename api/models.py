from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Teste(models.Model):
    test = models.CharField(max_length=15)
    number = models.IntegerField()

class User(AbstractUser):
    email = models.EmailField(unique=True)
    