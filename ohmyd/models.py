from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="")
    secret = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)