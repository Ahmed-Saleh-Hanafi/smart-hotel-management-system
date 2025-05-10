
from checkinout.models import CheckIn , CheckOut
from django.utils import timezone

def check_in_guest(guest, room):
    checkin = CheckIn.objects.create(
        guest=guest,
        room=room,
        check_in_time=timezone.now()
    )
    room.status = 'occupied'
    room.save()
    return checkin

def check_out_guest(checkin, feedback=''):
    checkout = CheckOut.objects.create(
        checkin=checkin,
        check_out_time=timezone.now(),
        feedback=feedback
    )
    room = checkin.room
    room.status = 'cleaning'  
    room.save()
    return checkout