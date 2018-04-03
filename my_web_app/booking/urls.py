from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('available_rooms/<int:year>/<int:month>/<int:day>/', views.available_rooms),
]