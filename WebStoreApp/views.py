from django.forms import ModelForm
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import *
from django import forms
import random
from WebStoreApp.Infraestructure.Persistence.ProductBrandRepository import ProductBrandRepository 
from WebStoreApp.Application.Services.ProductBrandApplicationService import ProductBrandApplicationService
from WebStoreApp.Application.Commands.CreateProductBrandCommand import CreateProductBrandCommand
from WebStoreApp.Application.Handlers.CreateProductBrandHandler import CreateProductBrandHandler
# Create your views here.

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender_id', 'document']

class ProductBrandForm(ModelForm):
    class Meta:
        model = ProductBrand
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full px-4 py-2 rounded-lg border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Type the brand name'}),
        }


def person_store(request, template_name='person/person_form.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    
    return render(request=request, template_name=template_name,context={'form':form})

def person_list(request, template_name='person/person_list.html'):
    query = request.GET.get('search')
    if query:
        person = Person.objects.filter(first_name__icontains=query)
    else:
        person = Person.objects.all()

    return render(request, template_name, {'list':person})


def story_home(request, template_name='story/home.html'):
    query = request.GET.get('search')
    if query:
        products = Person.objects.filter(first_name__icontains=query)
    else:
        products = Person.objects.all()

    products = [

    ]
    for i in range(1,50):
        price = random.randint(20,99)
        products.append({"pk":i,'name': f'Product {i}', 'price': price, f'description':'Short product description'})

    return render(request, template_name, {'products':products})

def product_details(request, pk, template_name='story/product_details.html'):
    #product = get_object_or_404(Product, pk=pk)
    product = None
    reviews =  [
        {'rating':5, 'user':'Test', 'comment':'Test'}
    ] 
    return render(request, template_name, {'element': product, 'reviews':reviews})

def brand_list(request, template_name='product_brand/brand_list.html'):
    query = request.GET.get('search')
    if query:
        items = ProductBrand.objects.filter(name__icontains=query).order_by('-id')
    else:
        items = ProductBrand.objects.all().order_by('-id')

    return render(request, template_name, {'items':items})


def brand_create(request, template_name="product_brand/brand_form.html"):
    
    brand_handler = CreateProductBrandHandler(ProductBrandRepository())
    brand_service = ProductBrandApplicationService()
    brand_service.create_brand_handler=brand_handler

    
    form = ProductBrandForm(request.POST or None)
    if form.is_valid():
        #prod_brand = form.save(commit=False)
        #prod_brand.active='1'
        #prod_brand.save()
        
        name = form.cleaned_data['name']
        brand_command = CreateProductBrandCommand()
        brand_command.id = None
        brand_command.name = name
        brand = brand_service.create_brand(brand_command)
        return redirect('brand_list')
    
    return render(request, template_name, {'form': form})

def brand_edit(request, pk, template_name='product_brand/brand_form.html'):
    brand = get_object_or_404(ProductBrand, pk=pk)
    brand_handler = CreateProductBrandHandler(ProductBrandRepository())
    brand_service = ProductBrandApplicationService()
    brand_service.create_brand_handler=brand_handler

    if request.method == 'POST':
        form = ProductBrandForm(request.POST, instance=brand)
        if form.is_valid():
            name = form.cleaned_data['name']
            brand_command = CreateProductBrandCommand()
            brand_command.id = pk
            brand_command.name = name
            brand = brand_service.create_brand(brand_command)
            #form.save()
            return redirect('brand_list')
    else:
        form = ProductBrandForm(instance=brand)
    
    return render(request, template_name, {'form':form})

def brand_delete(request, pk, template_name="product_brand/delete_form.html"):
    item = ProductBrand.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('brand_list')
    return render(request, template_name, {'item':item})


def index(request):
    return HttpResponse("Hello, world. You're at the Web Store index Project")
