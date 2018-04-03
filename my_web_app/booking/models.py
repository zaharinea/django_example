from django.db import models

# Create your models here.


class Room(models.Model):
    number = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    smoke = models.NullBooleanField(blank=True, null=True)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)