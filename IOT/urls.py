

from django.urls import path 
from . import views

urlpatterns = [
 path ('room_control/', views.room_control, name='room_control'),
]
