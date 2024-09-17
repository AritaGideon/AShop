from django.db import models


class Order(models.Model):
    order_id = models.CharField()
    price_total = models.FloatField(max_length=6)
    customer_information = models.CharField()


