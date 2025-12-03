from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

# def greeting(request):
#     if request.GET:
#         return render (request, 'formdata.html', {
#             'fromData' : request.GET
#         })
#     return render(request,'index.html')

from django.shortcuts import render, redirect
# from .forms import LoginForm

# def greeting(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return render(request,'form-data.html',{
#                  'email': form['email'].value
#              })
#     else:
#         form = LoginForm()
#     return render(request,'index.html',{'form':form})

from .models import Customer
from django.http import HttpResponse

# def greeting(request):
#     cust = Customer()
#     cust.email = 'user2@mashupstack.com'
#     cust.password = 'hello123'
#     cust.save()
#     return HttpResponse('DB table row created')

# def greeting (request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid:
#             cust = Customer()
#             cust.email = 'user2@mashupstack.com'
#             cust.password = 'hello123'
#             cust.save()
#             return render(request, 'formdata.html', {
#                 'message' : 'Data saved to DB'
#             })
#     else:
#         form = LoginForm()
#     return render(request, 'index.html', {'form' : form})

from .forms import LoginModelForm


# def greeting (request):
#     if request.method == 'POST':
#         form = LoginModelForm(request.POST)
#         if form.is_valid():
#             cust = form.save()
#             return render (request, 'formdata.html', {
#                 'message': 'Data saved to DB',
#             })
#     else:
#         form = LoginModelForm()
#     return render(request, 'index.html', {'forms' : form})



# def greeting (request):
#     if request.method == 'POST':
#         form = LoginModelForm(request.POST)
#         if form.is_valid():
#             cust = form.save()
#             return render (request, 'formdata.html', {
#                 'message': 'Data saved to DB',
#                 'Customer' : cust
#             })
#     else:
#         form = LoginModelForm()
#     return render(request, 'index.html', {'forms' : form})
@login_required(login_url='/login/')
def greeting (request):
    data = Customer.objects.all()
    return render (request, 'index.html', {'data' : data})

# def greeting (request):
#     data = Customer.objects.all().values('id','email')
#     return render (request, 'index.html', {'data' : data})
@login_required(login_url='/login/')
def aboutus (request):
    return render(request, 'aboutus.html')
@login_required(login_url='/login/')
def pages (request, title):
    return render (request, 'pages.html', {
        'title' : title
    })
@login_required(login_url='/login/')
def count (request, num):
    return render (request, 'count.html', {
        'num' : num
    })
@login_required(login_url='/login/')
def pagevisit(request):
    count = request.session.get('page_count', 0)
    count += 1
    request.session['page_count'] = count
    return render (request, 'pageview.html', {
        'count' : count
    })



from django.contrib.auth.forms import UserCreationForm
@login_required(login_url='/login/')
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('createproduct')
        
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {
        'form' : form
    })

@login_required(login_url='/login/')
def login_page(request):
    print("hi")
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    else:
        form = AuthenticationForm()

    return render (request, 'login.html', {
           'form' : form
    })

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)