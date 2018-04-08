from django.urls import path

from . import views


urlpatterns = [
    path('room/create', views.create_room),
    path('room/read/<int:room_id>', views.read_room),
    path('room/update/<int:room_id>', views.update_room),
    path('room/delete/<int:room_id>', views.delete_room),
    path('current_orders/<int:year>/<int:month>/<int:day>/',
         views.current_orders),
]
