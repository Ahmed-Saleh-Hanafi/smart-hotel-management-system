from django.db import models
from datetime import datetime
# Create your models here.

ROLE = [
        ('manager', 'Manager'),
        ('receptionist', 'Receptionist'),
        ('housekeeping', 'Housekeeping'),
    ]

Gender = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O','Other')
]

class Guest(models.Model):
    primary_id = models.AutoField(primary_key=True)
    username = models.CharField (max_length= 30, blank= True)
    date_joined = models.DateTimeField (default= datetime.now)
    last_login = models.DateTimeField (default= datetime.now)
    password = models.CharField (max_length= 20, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=20, blank= True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    country = models.CharField(max_length= 20, blank=True)
    is_active = models.BooleanField(default=True)
    code_to_active = models.IntegerField (default= 99999, blank=True)
    gender = models.CharField (max_length=1 , choices= Gender, default='O', blank=True)
    temp_password = models.CharField (max_length= 20, blank=False, default='#######')
    
    def __str__(self):
        return self.username
    
    class Meta ():
        verbose_name = 'Guest'
        ordering = ['primary_id']
    
class Employee (Guest):
    salary = models.DecimalField(max_digits= 5,decimal_places= 3)
    role = models.CharField (max_length=20, choices=ROLE, default='receptionist')
    
