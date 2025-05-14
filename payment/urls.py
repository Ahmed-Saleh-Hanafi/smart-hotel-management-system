

from django.urls import path 
from . import views
urlpatterns = [
    path('payment/<int:book_id>/', views.payment_page, name='payment'),
 
]
