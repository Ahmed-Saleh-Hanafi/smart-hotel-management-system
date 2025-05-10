from django.db import models

# Create your models here.
class RoomType(models.Model):
    room_type_id = models.AutoField (primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    max_guests = models.IntegerField(default=1)  
    floors = models.CharField(max_length=100, blank=True)  
    view = models.CharField(max_length=100, blank=True)  
    room_features = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    perfect_for = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta ():
        ordering = ['room_type_id']
        
    def room_count(self):
        return self.room_set.count()  
    

class Room(models.Model):  
    room_id = models.AutoField(primary_key= True)
    room_number = models.CharField (max_length=10)
    type = models.ForeignKey(RoomType, related_name='rooms' ,on_delete=models.CASCADE)
    phone_room = models.CharField(max_length=20, blank= True)
    status = models.CharField(max_length=20, choices=[
        ('vacant', 'Vacant'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance'),
    ], default='vacant')

    # IoT fields
    light_on = models.BooleanField(default=False)
    ac_on = models.BooleanField(default=False)
    ac_temperature = models.IntegerField(default=22)
    tv_on = models.BooleanField(default=False)
    curtains_open = models.BooleanField(default=True)
    do_not_disturb = models.BooleanField(default=False)
    door_locked = models.BooleanField(default=True) 
    
    def __str__(self):
        return f"{self.type} - Room {self.room_number}"

class RoomTypeImage(models.Model):
    type = models.ForeignKey(RoomType, related_name='images', on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='room_images/')
    
    def __str__(self):
        return f"{self.type}"

class RoomImage (models.Model):
    room =  models.ForeignKey (Room, related_name='images', on_delete= models.CASCADE)
    image = models.ImageField (upload_to='room_images/')
    
    def __str__ (self):
        return f"{self.room}"
