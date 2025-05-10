"""
URL configuration for Luxotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path ('',include ('Pages.urls'), name= 'Pages'),
    path ('management/', include('Accounts.urls'), name= 'Accounts'),
    path ('rooms/', include ('rooms.urls'), name= 'rooms'),
    path ("booking/", include ('booking.urls'), name='booking'),
    path ('checkinout/', include ('checkinout.urls'), name='checkinout'),
    path('staff/', include('staff.urls'), name='staff'),
    path('payment/', include('payment.urls'), name='payment'),
    path('iot/', include('IOT.urls'), name='iot'),
    path('chatbot/', include('chatbot.urls'), name='chatbot'),
    path('reports/', include('reports.urls'), name='reports'),
    path('AI_engine/', include('AI_engine.urls'), name='AI_engine'),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
