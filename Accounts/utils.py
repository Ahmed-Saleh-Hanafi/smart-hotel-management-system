import random
from django.core.mail import EmailMessage
from . import models


def send_email (subject, body, to_email):
    email = EmailMessage (
        subject= subject,
        body= body,
        from_email= 'luxotel.smarthotel@gmail.com',
        to= [to_email],
    )
    email.send()

def create_save_get_gest (request):
    username = request.POST.get ('rusername')
    email = request.POST.get ('remail')
    phone = request.POST.get ('rphone')
    password = request.POST.get ('rpassword')
    code_to_active = random.randint (10000, 99999)
    guest = models.Guest (username= username, email= email, phone_number= phone, password= password, code_to_active= code_to_active)
    guest.save ()
    return guest

def send_verification_email(user):
    send_email ('verification message to email before granting access',
                f'''Welecome {user.username}
                This is verification message to your email before granting access to our website
                This is your verification code {user.code_to_active}''',
                user.email
                )
   
def send_reset_password_to_email (user):
    user.temp_password = random.randint (10000000, 99999999)
    send_email ('Reset password message ',
                f'''Welcom {user.username} !,
                This is reset password message 
                This is your password  {user.temp_password}''',
                user.email)
    user.save ()

def get_guest_by_email (email):
    try:
        guest = models.Guest.objects.get (email= email)
    except models.Guest.DoesNotExist:
        guest = None
    return guest

def get_guest_by_id (id):
    try:
        guest = models.Guest.objects.get (primary_id= id)
    except models.Guest.DoesNotExist:
        guest = None
    return guest

def delete_guest_by_id (guest_id):
    guest = get_guest_by_id (guest_id)
    if guest:  models.Guest.objects.get (primary_id= guest_id).delete()
    
def create_session (request, user_id):
    request.session['user_id'] = user_id
    request.session.set_expiry(3600)  #  session expires in 1 hour
