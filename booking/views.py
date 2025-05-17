from django.shortcuts import render, redirect , get_object_or_404
from rooms.models import Room 
from Accounts import  utils
from .models import Booking
# Create your views here.


def book_page (request, room_id):
    id = request.session.get('user_id')
    guest_info= utils.get_guest_by_id(id)
    room = get_object_or_404(Room, pk=room_id)
    
    dic = {
        'name_page':'Luxotel | Room Info',
        'guest_info': guest_info,
        'room': room,
    }
    return render (request,'test2.html')

