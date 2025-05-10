

from . import models

def get_room_types (num):
    room_types = models.RoomType.objects.all()
    return room_types

def rooms_grouped_by_type():
    room_types2 = models.RoomType.objects.prefetch_related('room_set')

def get_rooms():
    return models.Room.objects.all()