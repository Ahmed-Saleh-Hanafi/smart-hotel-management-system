from django.shortcuts import render, get_object_or_404
from Accounts import utils
from booking.models import Booking 
from booking import book_utils
# Create your views here.
def payment_page(request, book_id):
    id = request.session.get('user_id')
    guest_info= utils.get_guest_by_id(id)
    book = get_object_or_404(Booking, pk=book_id)
    number_of_days = (book.check_out - book.check_in).days
    dic = {
        'name_page':'Luxotel | Payment Info',
        'guest_info': guest_info,
        'book': book,
        'ndays': number_of_days,
    }
    return render (request, 'Pages/payment.html', dic)
    