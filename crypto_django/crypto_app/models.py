from django.db import models
# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class coin(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    market_cap = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
