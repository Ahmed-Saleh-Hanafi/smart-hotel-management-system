from django.shortcuts import render
from Accounts import utils
# Create your views here.
def room_control (request):
    id = request.session.get('user_id')
    guest_info = utils.get_guest_by_id (id)
    dic = {
        'name_page':'Luxotel | Room Control',
        'guest_info': guest_info,
    }
    return render (request,'Pages/room_control.html', dic)