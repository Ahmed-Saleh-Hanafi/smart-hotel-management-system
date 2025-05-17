

from django.urls import path 
from . import views
urlpatterns = [
 path ('manager/',views.manager, name='manager'),
 path('manger_delete_room/<int:room_id>/', views.delete_room, name='manger_delete_room'),
 path ('manage_rooms/', views.manage_rooms, name='manage_rooms'),
 path('manager_edit_room/<int:room_id>/', views.edit_room, name='manger_edit_room'),
 path ('receptionist/', views.receptionist, name='receptionist'),
 path ('receptionist_booking/', views.receptionist_booking, name='receptionist_booking'),
 path ('receptionist_Guests/', views.receptionist_Guests , name='receptionist_Guests'),
 path ('receptionist_rooms/', views.receptionist_rooms , name='receptionist_rooms'),
 path ('receptionist_rooms_types/', views.receptionist_rooms_types , name='receptionist_rooms_types'),
  path ('receptionist_checkin/', views.receptionist_checkin, name='receptionist_checkin'),
  path ('receptionist_checkout/', views.receptionist_checkout, name='receptionist_checkout'),
 
]
