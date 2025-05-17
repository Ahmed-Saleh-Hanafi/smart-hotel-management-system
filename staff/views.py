from django.shortcuts import render, redirect, get_object_or_404
from . import staff_utils
from rooms.models import Room , RoomType , RoomImage
from Accounts.models import Guest 
from booking.models import Booking
from django.db.models import Q
# Create your views here.
def manager (request):
    id = request.session.get('user_id')
    manager= staff_utils.get_manager_by_id(id)
    rooms = Room.objects.all()
    dic = {
        'name_page':'Luxotel | Management',
        'manager': manager,
        'rooms': rooms,
    }
    return render (request, 'base_manager.html',dic)

def manage_rooms (request):
    id = request.session.get('user_id')
    manager= staff_utils.get_manager_by_id(id)
    rooms = Room.objects.all()
    dic = {
        'name_page':'Luxotel | Manage Rooms',
        'manager': manager,
        'rooms': rooms,
    }
    return render (request, 'PartsManager/rooms.html',dic)

def delete_room(request, room_id):
    room = get_object_or_404(Room, room_id=room_id)
    room.delete()
    return redirect('manage_rooms') 

def edit_room (request, room_id):
    id = request.session.get('user_id')
    manager= staff_utils.get_manager_by_id(id)
    room = get_object_or_404(Room, room_id=room_id)
    room_types = RoomType.objects.all()
    dic = {
        'name_page':'Luxotel | Edit Room',
        'manager': manager,
        'room': room,
        'room_types': room_types,
    }
    room2 = room
    if request.method == "POST":
        if request.FILES.get ('image'):
            image_file = request.FILES.get ('image')
            x = RoomImage() 
            x.room = room2
            x.image = image_file
            x.save()
        if request.POST.get ('roomNumber'):
            room2.room_number = request.POST.get ('roomNumber')
        room2.save ()
        room = room2
        dic['room'] = room
        return render (request,'PartsManager/edit_rooms.html',dic | {'success':'update room'})
    return render (request,'PartsManager/edit_rooms.html',dic )






###@@@@ Reception

def receptionist(request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    
    dic = {
        'name_page':'Luxotel | Management | receptionist',
        'receptionist': receptionist ,
    }
    return render (request, 'base_receptionist.html',dic)


def receptionist_booking (request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    books = Booking.objects.all()
    dic = {
        'name_page':'Luxotel | Management | receptionist | booking',
        'receptionist': receptionist ,
        'books': books,
    }
    return render (request, 'PartsReception/reception_booking.html',dic)

def receptionist_Guests (request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    guests =  Guest.objects.exclude(Q(is_email_verified=False))
    dic = {
        'name_page':'Luxotel | Management | receptionist | Guests',
        'receptionist': receptionist ,
        'guests': guests,
    }
    return render (request, 'PartsReception/receptionist_guests.html',dic)

def receptionist_rooms (request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    rooms = Room.objects.all ()
    dic = {
        'name_page':'Luxotel | Management | receptionist | rooms',
        'receptionist': receptionist ,
        'rooms': rooms,
    }
    return render (request, 'PartsReception/receptionist_rooms.html',dic)

def receptionist_rooms_types (request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    rooms_types = RoomType.objects.all()
    dic = {
        'name_page':'Luxotel | Management | receptionist | rooms types',
        'receptionist': receptionist ,
        'rooms_types':rooms_types,
    }
    return render (request, 'PartsReception/receptionist_room_types.html',dic)

def receptionist_checkin (request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    books = Booking.objects.filter(status='check_in')
    dic = {
        'name_page':'Luxotel | Management | receptionist | check-in',
        'receptionist': receptionist ,
        'books': books,
    }
    return render (request, 'PartsReception/receptionist_checkin.html',dic)

def receptionist_checkout (request):
    id = request.session.get('receptionist_id')
    receptionist= staff_utils.get_receptionist_by_id(id)
    books = Booking.objects.filter(status='check_out')
    dic = {
        'name_page':'Luxotel | Management | receptionist | check out',
        'receptionist': receptionist ,
        'books': books,
    }
    return render (request, 'PartsReception/receptionist_checkout.html',dic)