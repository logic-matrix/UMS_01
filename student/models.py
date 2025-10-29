from django.db import models
from django.utils.html import format_html, mark_safe
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

 