from django.forms import ModelForm
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from .models import *
import random
# Create your views here.

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender_id', 'document']

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
        products.append({'name': f'Product {i}', 'price': price, f'description':'Short product description'})

    return render(request, template_name, {'products':products})

def index(request):
    return HttpResponse("Hello, world. You're at the Web Store index Project")
