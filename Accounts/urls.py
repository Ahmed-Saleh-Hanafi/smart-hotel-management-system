from django.urls import path , include
from . import views
urlpatterns = [
   path ('exit_profile', views.exit_profile, name='exit_profile'),
   path ('profile_setting/', views.profile_setting, name = 'profile_setting'),
   path ('verification/', views.verification_code, name= 'verification_code'),
   path ('delete_account/', views.delete_account, name='delete_account'),
   path ('booking_history/', views.booking_history, name = 'booking_history'),
   path ('exit_profile_receptionist/', views.exit_profile_receptionist, name='exit_profile_receptionist'),
]
