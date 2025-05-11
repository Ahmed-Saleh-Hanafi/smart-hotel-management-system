
from django.urls import path 
from . import views
urlpatterns = [
    path ('booking/<int:room_id>/', views.book_page, name='book_page'),
]
