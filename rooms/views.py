from django.shortcuts import render , get_object_or_404
from Accounts import utils
from rooms import utils as utils_rooms
from .models import RoomType , Room
# Create your views here.

def rooms (request):
    id = request.session.get('user_id')
    guest_info= utils.get_guest_by_id(id)
    room_types = utils_rooms.get_room_types (10)
    rooms_ = utils_rooms.get_rooms ()
    dic = {
        'name_page':'Luxotel | Rooms',
        'guest_info': guest_info,
        'room_types': room_types,
        'rooms_': rooms_,
    }
    return render (request, 'Pages/rooms.html',dic)


def room_type_detail (request, room_type_id):
    id = request.session.get('user_id')
    guest_info= utils.get_guest_by_id(id)
    room_type = get_object_or_404(RoomType, pk=room_type_id)
    
    dic = {
        'name_page':'Luxotel | Room Type',
        'guest_info': guest_info,
        'room_type': room_type,
    }
    return render (request, 'Pages/room_type.html',dic)

def room_detail (request, room_id):
    id = request.session.get('user_id')
    guest_info= utils.get_guest_by_id(id)
    room = get_object_or_404(Room, pk=room_id)
    
    dic = {
        'name_page':'Luxotel | Room Info',
        'guest_info': guest_info,
        'room': room,
    }
    return render (request, 'Pages/room.html',dic)
    