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
    deleted_at = models.DateTimeField(null=True, default=None)
    created_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name='created_%(class)s_set')
    updated_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name='updated_%(class)s_set')
    deleted_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name='deleted_%(class)s_set')
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)

    class Meta:
        abstract = True


class Gender(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The gender's name")

class Person(BaseModel):
    first_name = models.CharField(max_length=255, null=False, help_text="The person's first name")
    last_name = models.CharField(max_length=255, null=True, blank=True, default=None, help_text="The person's last name")
    social_name = models.CharField(max_length=255, null=True, blank=True, default=None, help_text="The person's social name")
    document = models.CharField(max_length=255, null=False, help_text="The person's document, like the person ID")
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)

class Branch(BaseModel):
    root_id = models.ForeignKey('self',null=None, blank=True, help_text="The root branch id", on_delete=models.CASCADE)
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
    number = models.CharField(max_length=500, null=True, blank=True, default=None)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

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
    product_depart_id = models.ForeignKey(ProductDepartment, on_delete=models.CASCADE,help_text="The product department table id")
    product_category_id = models.ForeignKey('self', on_delete=models.CASCADE,null=None, blank=True, help_text="The product category table id")

class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, help_text="The product's name")
    product_brand_id = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    product_category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,help_text="The product category table id")

class Stock(BaseModel):
    DEFAULT_STOCK = [
        ('1','Yes'),
        ('0','No'),
    ]
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, help_text="The stock's name")
    available_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Available quantity in stock")
    blocked_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Blocked quantity in stock")
    reserved_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Reserved quantity in stock")
    damaged_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Damaged quantity in stock")
    fiscal_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Fiscal quantity in stock")
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE,help_text="The branch table id")
    is_default = models.IntegerField(max_length=1, choices=DEFAULT_STOCK, default=0, help_text="The default stock")

class StockInventory(BaseModel):
    TYPE = [
        ('1','Incoming'),
        ('0','Outgoing'),
    ]
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE,help_text="The stock table id")
    previous_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Previous quantity in stock")
    moved_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Moved quantity in stock")
    current_quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Current quantity in stock")
    inventory_type = models.IntegerField(max_length=1, choices=TYPE, help_text="Type of stock inventory")
    reference = models.IntegerField(null=True, default=None, help_text="The origin of the stock inventory, can be a table name")
    reference_id = models.IntegerField(null=True, default=None ,help_text="The origin id of the stock inventory, can be a table id")

class Sale(BaseModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE,help_text="The person table id")
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE,help_text="The branch table s id")
    person_address_id = models.ForeignKey(PersonAdress, on_delete=models.CASCADE,help_text="The person table address's id")
    sale_total = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Total gross sales value amount, only products")
    sale_discount = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Sale discount amount")
    sale_shipping = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Sale shipping amount")
    sale_net_amount = models.DecimalField(max_digits=60, decimal_places=6, default=0, null=True, help_text="Total sale amount: product-discount+frete")
    
#https://docs.djangoproject.com/en/5.0/ref/models/fields/