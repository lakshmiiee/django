from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contactus'),
    path('form', views.contactform, name='contactform'),    
]