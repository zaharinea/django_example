from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.urls import path, include

from . import views


router = routers.DefaultRouter()
router.register(r'room', views.RoomViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view)
]