from django.db import models

class Product(models.Model):
    date = models.DateField()
    provider = models.CharField(max_length=50)
    name_of_product = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    stock = models.IntegerField()

