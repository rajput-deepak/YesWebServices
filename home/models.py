from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class saveMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    msg = models.TextField()