from django.db import models
from django.forms import EmailField

# Create your models here.


class UserDetails(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.username
