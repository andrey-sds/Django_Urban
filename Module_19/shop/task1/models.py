from django.db import models
from django.utils import timezone


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(default='')
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


