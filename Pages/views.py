from django.shortcuts import render , redirect
from Accounts import utils
from rooms import utils as utils_rooms
from staff import staff_utils
# Create your views here.


def index (request):
    id = request.session.get('user_id')
    guest_info= utils.get_guest_by_id(id)
    room_types = utils_rooms.get_room_types (10)
    rooms_ = utils_rooms.get_rooms ()
    #---------------------------  Registration ---------------------#
    if request.method == 'POST' and request.POST.get ('rusername'):
        print ('hi')
        email = request.POST.get ('remail')
        guest = utils.get_guest_by_email (email)
        if guest :
            return render (request,  'Pages/index.html', {'error': 'Email is already is registred', 'name_page':'Luxotel | home' , 'room_types':room_types,'rooms_': rooms_})
        else :
            guest = utils.create_save_get_gest (request)
            utils.send_verification_email (guest)
            utils.create_session (request, guest.primary_id)
            return redirect ('verification_code')
        
    #------------------------------ Login -----------------------------#
    elif request.method == 'POST' and request.POST.get ('spassword'):
        email = request.POST.get ('semail')
        password = request.POST.get ('spassword')
        manger = staff_utils.is_manager (email,password)
        if manger:
            utils.create_session (request, manger.primary_id)
            return redirect ('manager')
            ######receptionist
        receptionist = staff_utils.is_receptionist(email,password)
        if receptionist:
            staff_utils.create_session_receptionist(request, receptionist.primary_id)
            return redirect ('receptionist') 
          #########
        guest = utils.get_guest_by_email (email)
        if guest and (guest.password == password or password == guest.temp_password) :
            if  guest.is_email_verified:
                utils.create_session (request, guest.primary_id)
                guest_info = utils.get_guest_by_id (guest.primary_id)
                return render(request, 'Pages/index.html', { 'guest_info': guest_info,'name_page':'Luxotel | home' , 'room_types':room_types, 'rooms_': rooms_})
            else :
                utils.delete_guest_by_id(guest.primary_id)
                return render (request,  'Pages/index.html', {'error': 'your email is not verified, try to register again',  'name_page':'Luxotel | home',  'room_types':room_types, 'rooms_': rooms_})
                
        else:
            return render (request,  'Pages/index.html', {'error': 'Invalid email or password', 'name_page':'Luxotel | home' , 'room_types':room_types, 'rooms_': rooms_})
        
    #----------------------------- Reset password---------------------
    elif request.method == 'POST' :
        email = request.POST.get ('resetemail')
        guest = utils.get_guest_by_email (email)
        if guest:
            utils.send_reset_password_to_email (guest)
            return render (request,  'Pages/index.html', {'success': 'send a new passwoed to your email', 'name_page':'Luxotel | home', 'room_types':room_types, 'rooms_': rooms_})
        else :
            return render (request,  'Pages/index.html', {'error': 'this email is not correct' , 'name_page':'Luxotel | home', 'room_types':room_types, 'rooms_': rooms_})
    
    #------------------------------- index page------------------------
    return render(request, 'Pages/index.html', { 'guest_info': guest_info,'name_page':'Luxotel | home', 'room_types':room_types, 'rooms_': rooms_})




    