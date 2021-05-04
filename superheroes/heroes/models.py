from django.db import models

class Hero(models.Model):
    name = models.CharField(nax_length=50)
    identity = models.CharField(nax_length=50)
    primary = models.CharField(nax_length=50)
    secondary = models.CharField(nax_length=50)
    catchphrase = models.CharField(nax_length=50)
