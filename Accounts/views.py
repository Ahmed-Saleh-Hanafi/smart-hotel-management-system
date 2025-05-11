from django.shortcuts import render , redirect
from . import utils


def verification_code (request):
     if request.method == 'POST' :
        code = request.POST.get('v_code')
        id = request.session.get('user_id')
        guest = utils.get_guest_by_id(id)
        code = str (code)
        code_guest = str (guest.code_to_active)
        
        if code ==  code_guest:
            guest.is_email_verified = True
            guest.save()
            return redirect ('index')
        else :
            return render (request, 'Pages/verification.html', {'error': 'code is not correct', 'name_page':'Luxotel | verification'})
     return render (request, 'Pages/verification.html', {'name_page':'Luxotel | verification'})
 
def profile_setting (request):
    id = request.session.get('user_id')
    guest_info = utils.get_guest_by_id (id)
    guest= utils.get_guest_by_id (id)
    if request.method == "POST":
        if request.POST.get ('username'):
            guest.username = request.POST.get ('username')
        if request.POST.get ('phone'):
            guest.phone_number = request.POST.get ('phone')
        if request.POST.get ('phone'):
            guest.phone_number = request.POST.get ('phone')
        if request.POST.get ('gender'):
            guest.gender = request.POST.get ('gender')[0]
        if request.POST.get ('country'):
            guest.country = request.POST.get ('country')
        if request.POST.get ('password'):
            guest.password = request.POST.get ('password')
        if request.FILES.get ('image'):
            image_file = request.FILES.get ('image')
            guest.profile_picture = image_file 
        guest.save ()
        guest_info = guest
        return render (request,'Pages/profile_setting.html', {'success': 'you update your account', 'guest_info': guest_info})
    return render (request,'Pages/profile_setting.html', {'guest_info': guest_info})

def booking_history (request):
    id = request.session.get('user_id')
    guest_info = utils.get_guest_by_id (id)
    guest= utils.get_guest_by_id (id)
    return render (request,'Pages/booking_history.html', {'guest_info': guest_info})

def exit_profile (request):
    del request.session['user_id']
    return redirect ('index')

def delete_account (request):
    id = request.session.get('user_id')
    utils.delete_guest_by_id (id)
    return redirect ('exit_profile') 




