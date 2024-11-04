from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

# Create your models here.
