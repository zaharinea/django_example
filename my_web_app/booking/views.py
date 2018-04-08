import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

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
    return JsonResponse(model_to_dict(room))

def read_room(request, room_id):
    room = Room.objects.get(id=room_id)
    return JsonResponse(model_to_dict(room))

def update_room(request, room_id):
    r = json.loads(request.body.decode("utf-8"))
    Room.objects.filter(id=room_id).update(**r)
    return JsonResponse(r)

def delete_room(request, room_id):
    Room.objects.filter(id=room_id).delete()
    return HttpResponse()
