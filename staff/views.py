from django.shortcuts import render, redirect, get_object_or_404
from . import staff_utils
from rooms.models import Room , RoomType , RoomImage
from django.http import JsonResponse
# Create your views here.
def manager (request):
    id = request.session.get('user_id')
    manager= staff_utils.get_manager_by_id(id)
    rooms = Room.objects.all()
    dic = {
        'name_page':'Luxotel | Management',
        'manager': manager,
        'rooms': rooms,
    }
    return render (request, 'base_manager.html',dic)

def manage_rooms (request):
    id = request.session.get('user_id')
    manager= staff_utils.get_manager_by_id(id)
    rooms = Room.objects.all()
    dic = {
        'name_page':'Luxotel | Manage Rooms',
        'manager': manager,
        'rooms': rooms,
    }
    return render (request, 'PartsManager/rooms.html',dic)

def delete_room(request, room_id):
    room = get_object_or_404(Room, room_id=room_id)
    room.delete()
    return redirect('manage_rooms') 

def edit_room (request, room_id):
    id = request.session.get('user_id')
    manager= staff_utils.get_manager_by_id(id)
    room = get_object_or_404(Room, room_id=room_id)
    room_types = RoomType.objects.all()
    dic = {
        'name_page':'Luxotel | Edit Room',
        'manager': manager,
        'room': room,
        'room_types': room_types,
    }
    room2 = room
    if request.method == "POST":
        if request.FILES.get ('image'):
            image_file = request.FILES.get ('image')
            x = RoomImage() 
            x.room = room2
            x.image = image_file
            x.save()
        if request.POST.get ('roomNumber'):
            room2.room_number = request.POST.get ('roomNumber')
        room2.save ()
        room = room2
        dic['room'] = room
        return render (request,'PartsManager/edit_rooms.html',dic | {'success':'update room'})
    return render (request,'PartsManager/edit_rooms.html',dic )