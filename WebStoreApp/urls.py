from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name='index'),
    path("home/", views.story_home, name='story_home'),
    path("person/register/", views.person_store, name='person_register'),
    path("person/list/", views.person_list, name='person_list'),
    path("product/details/<int:pk>", views.product_details, name='product_details'),
    path("brand/list/", views.brand_list, name='brand_list'),
    path("brand/create/", views.brand_create, name='brand_create'),
    path("brand/edit/<int:pk>", views.brand_edit, name='brand_edit'),
    path("brand/delete/<int:pk>", views.brand_delete, name='brand_delete'),
    path("brand/delete/<int:pk>", views.brand_delete, name='add_to_cart'),
    #path('editar_carro/<int:pk>', editar_carro, name='editar_carro'),
]
