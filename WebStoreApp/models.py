from django.db import models

# Create your models here.


class User(models.Model):
    VERIFIED_USER = [
        ('1','Yes'),
        ('0','No'),
    ]

    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]

    email = models.CharField(max_length=500, null=False)
    password = models.CharField(max_length=255, null=False)
    verified_user = models.IntegerField(max_length=1, choices=VERIFIED_USER)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE )

class Gender(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]

    name = models.CharField(max_length=255, null=False)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE )

class Person(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=True)
    social_name = models.CharField(max_length=255, null=True)
    document = models.CharField(max_length=255, null=False)
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)

class Country(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]
    name = models.CharField(max_length=500, null=False)
    code = models.CharField(max_length=100, null=True)
    acronym = models.CharField(max_length=50, null=True)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)

class State(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]
    name = models.CharField(max_length=500, null=False)
    code = models.CharField(max_length=100, null=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)

class City(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]
    name = models.CharField(max_length=500, null=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)

class PersonAdress(models.Model):
    ACTIVE_STORE = [
        ('1','Yes'),
        ('0','No'),
    ]
    street = models.CharField(max_length=500, null=False)
    zip_code = models.CharField(max_length=500, null=True)
    neighborhood = models.CharField(max_length=500, null=True)
    complement = models.CharField(max_length=500, null=True)
    active = models.IntegerField(max_length=1, choices=ACTIVE_STORE)