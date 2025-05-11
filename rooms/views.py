from django.shortcuts import render , get_object_or_404
from Accounts import utils
from rooms import utils as utils_rooms
from .models import RoomType , Room
from datetime import datetime 
from booking import book_utils
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
    date_now = datetime.now().date()
    ## manage check in date
    checkin_date = request.POST.get ('checkin_date')
    if checkin_date == '':
        return render (request, 'Pages/room.html',dic|{'error': 'you must set check in date'})
    elif request.POST.get ('checkin_date') :
        checkin_date2 = datetime.strptime(checkin_date, "%Y-%m-%d").date()
        if checkin_date2 < date_now:
            return render (request, 'Pages/room.html',dic|{'error': f'you must set check in date after {date_now}'})
        else :
            dic['checkin_date'] = checkin_date
    ## manage checkout date 
    checkout_date = request.POST.get ('checkout_date')
    if checkout_date == '':
        return render (request, 'Pages/room.html',dic|{'error': 'you must set check out date'})
    elif request.POST.get ('checkout_date'):
        checkout_date2 = datetime.strptime(checkout_date, "%Y-%m-%d").date()
        if checkout_date2 < checkin_date2 :
            return render (request, 'Pages/room.html',dic|{'error': f'you must set check out date after {checkin_date}'})
        else:
            dic['checkout_date'] = checkout_date
    ## manage number guest
    number_guest = request.POST.get ('number_guest')
    if request.POST.get ('number_guest'):
        if not number_guest.isdigit() :
            return render (request, 'Pages/room.html',dic|{'error': 'you must set number of guest as number'})
        elif int (number_guest) > room.type.max_guests:
            return render (request, 'Pages/room.html',dic|{'error': f'max guest is {room.type.max_guests}'})
        elif int (number_guest) < 1 :
            return render (request, 'Pages/room.html',dic|{'error': f'you must set number of guest as positive number'})
    elif number_guest == '':
        return render (request, 'Pages/room.html',dic|{'error': 'you must set number of guest'})
    # manage is avaliable or not
    if request.POST.get ('checkin_date') and request.POST.get ('checkout_date') and request.POST.get ('number_guest'):
        if book_utils.is_room_available (room_id,checkin_date2, checkout_date2):
            book_utils.create_booking (guest_info, room, checkin_date2, checkout_date2)
            ####payment
        else :
            return render (request, 'Pages/room.html',dic|{'error': 'this room is not availabe in this check in'})
            
        
        
    
    return render (request, 'Pages/room.html',dic)
    