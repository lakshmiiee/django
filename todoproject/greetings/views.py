from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from .models import Login

# Create your views here.
def greetings(request):
    #return HttpResponse ("Hello World..")
    return render(request,'index.html')

# def form(request):
#     if request.GET:
#         email= request.GET.get('email')
#         return render(request,'formdata.html',{
#             'formData':request.GET,
#             'email': email
#         })
#     return render(request,'form.html')

# def form(request):
#     if request.method == 'POST':
#         data = request.POST.copy()  # Make a mutable copy
#         data.pop('csrfmiddlewaretoken', None)  # Remove the CSRF token

#         email = data.get('email')  # use cleaned data, not request.POST

#         return render(request, 'formdata.html', {
#             'email': email,
#             'formData': data  # use cleaned data here
#         })
#     return render(request, 'form.html')

# def form(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             return render(request, 'formdata.html', {'email': email,
#                                                      'password':password})
#     else:
#         form = LoginForm()

#     return render(request, 'form.html', {'form': form})


def form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            log=Login()
            log.email=form.cleaned_data['email']
            log.password=form.cleaned_data['password']
            log.save()
            return render(request,'formdata.html',{
                 'message':'Data saved to db'
             })
    else:
        form = LoginForm()
    return render(request,'form.html',{'form':form})

# def login(request):
#     log1=Login()
#     log1.email='user1@gmail.com'
#     log1.password='user1234'
#     log1.save()
#     return HttpResponse("DB login row created")




