from django.db import models
from .fields import STATUS_CHOICES


class BrokerUser (models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    orderId = models.CharField(max_length=128)
    senderId = models.IntegerField()
    premiumUser = models.BooleanField(max_length=1)
    packageImage = models.CharField(max_length=1000)
    user = models.ForeignKey(BrokerUser,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)

    def __unicode__(self):
        return self.orderId

