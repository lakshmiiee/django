from django.shortcuts import render

def contactus(request):
    return render(request,'contact_us.html')

def contactusform(request):
    return render(request,'contact-us-form.html')