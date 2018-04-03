import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import Order


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def available_rooms(request, year, month, day):
    target_date = datetime.date(year=year, month=month, day=day)
    orders = Order.objects.filter(date_in__lte=target_date, date_out__gte=target_date)
    ord_ids = [str(order.id) for order in orders]
    res = '\n'.join(ord_ids)

    result = '{}/{}/{}'.format(year, month, day)
    return HttpResponse(res)