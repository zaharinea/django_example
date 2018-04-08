from django.db import models


class Room(models.Model):
    number = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "#{}".format(self.number)


class Client(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    smoke = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self):
        return "Order - id:{}, client:{}, room:{}, date_in:{:%y.%m.%d}, " \
               "date_out:{:%y.%m.%d}".format(self.id, self.client, self.room,
                                             self.date_in, self.date_out)