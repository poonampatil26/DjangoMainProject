from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def add(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')

    template_name = 'InventoryManagement/add.html'
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login')
def show(request):
    template_name = 'InventoryManagement/show.html'
    order = Product.objects.all()
    context = {'order': order}
    return render(request, template_name, context)

def update(request, id_f):
    order = Product.objects.get(id=id_f)
    form = ProductForm(instance=order)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'InventoryManagement/add.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete(request,id_f):
    order = Product.objects.get(id=id_f)
    order.delete()
    return redirect('show')


def home(request):
    template_name = 'InventoryManagement/home.html'
    context = {}
    return render(request, template_name, context)