from django.db import models
from django.utils import timezone
from  Accounts.models import Guest
from rooms.models import Room
# Create your models here.

class CheckIn(models.Model):
    checkin_id = models.AutoField (primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(default=timezone.now)
     
    def __str__(self):
        return f"{self.guest} checked in to {self.room}"

class CheckOut(models.Model):
    checkout_id = models.AutoField (primary_key=True)
    checkin = models.OneToOneField(CheckIn, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField(default=timezone.now)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.checkin.guest} checked out from {self.checkin.room}"