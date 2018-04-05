from django.urls import path

from . import views

urlpatterns = [
    path('room/create', views.create_room),
    path('current_orders/<int:year>/<int:month>/<int:day>/',
         views.current_orders),
]