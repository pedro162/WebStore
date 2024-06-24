from django.db import models

# Create your models here.

#Documentation: https://docs.djangoproject.com/en/5.0/topics/db/models/

class User(models.Model):
    VERIFIED_USER = [
        ('1','Yes'),
        ('0','No'),
    ]

    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]

    email = models.CharField(max_length=500, null=False, help_text="The user's email")
    password = models.CharField(max_length=255, null=False, help_text="The user's password")
    verified_user = models.IntegerField(max_length=1, choices=VERIFIED_USER)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

class BaseModel(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    created_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    updated_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    deleted_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)


class Gender(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The gender's name")

class Person(BaseModel):

    first_name = models.CharField(max_length=255, null=False, help_text="The person's first name")
    last_name = models.CharField(max_length=255, null=True, blank=True, default=None, help_text="The person's last name")
    social_name = models.CharField(max_length=255, null=True, blank=True, default=None, help_text="The person's social name")
    document = models.CharField(max_length=255, null=False, help_text="The person's document, like the person ID")
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)

class Branch(BaseModel):
    root_id = models.BigAutoField(null=None, blank=True, help_text="The root branch'id")
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

class Country(BaseModel):
    name = models.CharField(max_length=500, null=False)
    code = models.CharField(max_length=100, null=True, blank=True, default=None)
    acronym = models.CharField(max_length=50, null=True, blank=True, default=None)

class State(BaseModel):
    name = models.CharField(max_length=500, null=False)
    code = models.CharField(max_length=100, null=True, blank=True, default=None)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(BaseModel):
    name = models.CharField(max_length=500, null=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

class PersonAdress(BaseModel):
    street = models.CharField(max_length=500, null=False)
    zip_code = models.CharField(max_length=500, null=True, blank=True, default=None)
    neighborhood = models.CharField(max_length=500, null=True, blank=True, default=None)
    complement = models.CharField(max_length=500, null=True, blank=True, default=None)

class ProductUnit(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The unit's name")

class ProductPackage(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The package's name")
    product_unit_id = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    convert_quantity = models.DecimalField(max_digits=60, decimal_places=6,default=1, help_text="The convert quantity's value")

class ProductBrand(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The brand's name")

class ProductDepartment(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The depart's name")

class ProductCategory(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The category's name")
    product_depart_id = models.ForeignKey(ProductDepartment, on_delete=models.CASCADE,help_text="The product department's id table")
    product_categ_id = models.BigAutoField(null=None, blank=True, help_text="The product category's id table")

class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The product's name")
    product_brand_id = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    product_categ_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,help_text="The product category's id table")

#https://docs.djangoproject.com/en/5.0/ref/models/fields/