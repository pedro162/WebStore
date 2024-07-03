from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name='index'),
    path("home/", views.story_home, name='story_home'),
    path("person/register/", views.person_store, name='person_register'),
    path("person/list/", views.person_list, name='person_list'),
    #path('editar_carro/<int:pk>', editar_carro, name='editar_carro'),
]