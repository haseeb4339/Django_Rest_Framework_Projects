from django.db import models


class Customers(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
