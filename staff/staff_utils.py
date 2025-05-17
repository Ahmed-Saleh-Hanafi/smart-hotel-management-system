from Accounts.models import Employee

def get_manager_by_id (id):
    try:
        manager = Employee.objects.get (primary_id= id)
    except Employee.DoesNotExist:
        manager = None
    return manager

def is_manager (email, password):
    try:
        manager = Employee.objects.get (email= email, password= password, role='manager')
    except Employee.DoesNotExist:
        manager = None
    return manager

###############
def is_receptionist (email, password):
    try:
        receptionist = Employee.objects.get (email= email, password= password, role='receptionist')
    except Employee.DoesNotExist:
        receptionist = None
    return receptionist

def get_receptionist_by_id (id):
    try:
        receptionist = Employee.objects.get (primary_id= id)
    except Employee.DoesNotExist:
        receptionist = None
    return receptionist

def create_session_receptionist (request, user_id):
    request.session['receptionist_id'] = user_id
    request.session.set_expiry(3600)  #  session expires in 1 hour
    




