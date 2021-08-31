from django.db import models
from django.utils import timezone


class Offer(models.Model):
    rate = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    def __float__(self):
        return self.rate




class Market(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    address = models.CharField(max_length=255)
    phon_num = models.IntegerField()
    imag_url = models.CharField(max_length=2083)
    date_created = models.DateTimeField(default=timezone.now)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)