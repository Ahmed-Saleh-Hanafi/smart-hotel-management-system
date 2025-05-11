
from .models import Booking
from rooms.models import Room

import qrcode
from io import BytesIO
from django.core.files import File
from Accounts import utils


def generate_qr_code_for_checkin(booking):
    qr_data = f"CheckInID: {booking.booking_id} - Guest: {booking.guest.primary_id} - Room: {booking.room.room_id}"
    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer)
    filename = f"checkin_{booking.booking_id}.png"
    booking.qr_code.save(filename, File(buffer), save=True)
    
def get_available_rooms(check_in, check_out):
    booked_rooms = Booking.objects.filter(
        check_in__lt=check_out,
        check_out__gt=check_in,
        status__in=['pending', 'confirmed']
    ).values_list('room_id', flat=True)

    return Room.objects.exclude(id__in=booked_rooms)

def is_room_available(room_id, check_in, check_out):
    conflict_exists = Booking.objects.filter(
        room_id=room_id,
        status__in=['pending', 'confirmed'],
        check_in__lt=check_out,
        check_out__gt=check_in
    ).exists()

    return not conflict_exists

def create_booking (guest, room, checkin, checkout):
    number_of_days = (checkout - checkin).days
    toprice = number_of_days * room.type.base_price
    book = Booking (guest= guest,room= room, check_in= checkin, check_out=checkout,total_price= toprice)
    book.save ()
    generate_qr_code_for_checkin(book)