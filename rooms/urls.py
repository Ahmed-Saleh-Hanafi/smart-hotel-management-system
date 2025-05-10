
from django.urls import path 
from . import views
urlpatterns = [
   path ('rooms/', views.rooms, name='rooms'),
   path('room_type/<int:room_type_id>/', views.room_type_detail, name='room_type_detail'),
   path('room/<int:room_id>/', views.room_detail, name='room_detail'),
]
