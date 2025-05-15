

from django.urls import path 
from . import views
urlpatterns = [
 path ('manager/',views.manager, name='manager'),
 path('manger_delete_room/<int:room_id>/', views.delete_room, name='manger_delete_room'),
 path ('manage_rooms/', views.manage_rooms, name='manage_rooms'),
 path('manager_edit_room/<int:room_id>/', views.edit_room, name='manger_edit_room'),
]
