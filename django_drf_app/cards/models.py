from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
