from django.shortcuts import render, redirect
from booking.models import Booking
from rooms.models import Room
# Create your views here.

def check_in (request, book_id):
    book = Booking.objects.get (booking_id= book_id)
    book.status = 'check_in'
    room = Room.objects.get (room_id=book.room.room_id)
    room.status = 'occupied'
    room.save()
    book.save()
    return redirect ('receptionist_booking')

def check_out(request, book_id):
    book = Booking.objects.get (booking_id= book_id)
    book.status = 'check_out'
    room = Room.objects.get (room_id=book.room.room_id)
    room.status = 'cleaning'
    room.save()
    book.save()
    return redirect ('receptionist_checkin')