from django.db import models


class Subscribers(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, null=True)
    sex = models.CharField(max_length=128, default='M')
    date = models.DateField(format('dd.mm.yyyy'), null=True)
    test = models.CharField(max_length=128, default='test')
