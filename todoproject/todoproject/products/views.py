from django.shortcuts import render, redirect

# Create your views here.

from .froms import Productform
from .models import Product

def create(request):
    if request.method == 'POST':
        form = Productform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = Productform()
    
    return render (request, 'create.html', {
        'form' : form
    })

def product_read(request):
    product_list = Product.objects.all()
    return render (request, 'retrieve.html', {
        'product_list' : product_list
    })

def product_update(request, id):
    product = Product.objects.get(pk = id)

    if request.method == 'POST':
        form = Productform(request.POST, instance = product)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = Productform(instance = product)
    return render(request, 'update.html', {
        'form' : form
    })

def product_delete (request, pk):
    product = Product.objects.get(pk = pk)

    if request.method == 'POST':
        product.delete()
        return redirect ('home')
    
    return render (request, 'delete.html', {
        'product' : product
    })


# ===============================================================================================

from django.core.paginator import Paginator

def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)

    page_number = request.GET.get ('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)

    return render (request, 'list.html', {
        'page_obj' : page_obj
    })

