from django.db import models


class Categories(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    tags = models.CharField(max_length=25)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True, related_name='products')


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()





















