
from .models import Booking
from rooms.models import Room

import qrcode
from io import BytesIO
from django.core.files import File


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