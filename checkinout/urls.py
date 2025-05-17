
from django.urls import path 
from . import views
urlpatterns = [
   path ('check_in/<int:book_id>/', views.check_in, name='check_in'),
   path ('check_out/<int:book_id>/', views.check_out, name='check_out'),
]
