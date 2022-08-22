from django.db import models


class Pokemon(models.Model):
    text = models.CharField(max_length=200)
