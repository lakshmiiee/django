from django.urls import path
from . import views

urlpatterns = [

    path('', views.contactus,name='contact-us'),
    path('contactusform', views.contactusform,name='contact-us-form'),
]