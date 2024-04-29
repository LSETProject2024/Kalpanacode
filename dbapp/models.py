from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.firstname + "   " + self.lastname + "   " + self.phone

class Authentication(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username + "   " + self.password


class Payment(models.Model):
    amount = models.FloatField(null=True)
    paymentmethod = models.CharField(max_length=100)

    def __str__(self):
        return self.amount + "   " + self.paymentmethod





