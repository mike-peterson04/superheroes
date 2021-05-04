from django.db import models


class Hero(models.Model):
    hero_name = models.CharField(max_length=50)
    secret_identity = models.CharField(max_length=50)
    primary = models.CharField(max_length=50)
    secondary = models.CharField(max_length=50, null=True)
    catchphrase = models.CharField(max_length=50, null=True)
