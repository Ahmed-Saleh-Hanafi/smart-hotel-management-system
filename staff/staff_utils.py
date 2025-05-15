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
    




