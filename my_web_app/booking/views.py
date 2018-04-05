import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse

from .models import Order, Room


def current_orders(request, year, month, day):
    target_date = datetime.date(year=year, month=month, day=day)
    current_orders = Order.objects.filter(date_in__lte=target_date,
                                          date_out__gte=target_date)
    context = {'orders': current_orders}

    return render(request, 'booking/current_orders.html', context)

def create_room(request):
    r = json.loads(request.body.decode("utf-8"))
    room = Room(number=r['number'], price=r['price'])
    room.save()


    return JsonResponse(room.__dict__)