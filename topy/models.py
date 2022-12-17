from django.db import models

# Create your models here.
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    name = models.CharField("User Type Name", max_length=1024)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField("Email", max_length=254, unique=True)
    password = models.CharField("Password", max_length=40)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    name = models.CharField("Full Name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024,blank=True )
    address2 = models.CharField("Address line 2", max_length=1024,blank=True )
    zip_code = models.CharField("ZIP / Postal code", max_length=12, )
    city = models.CharField("City", max_length=1024, blank=True )
    birthday = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField("Gender", max_length=1, choices=GENDER_CHOICES, blank=True)
    phone = PhoneNumberField(null=False, blank=True)


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    name = models.CharField("Activity Name", max_length=1024)


class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Full Name", max_length=1024)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField("Gender", max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(null=True, blank=True)
    want_pet = models.BooleanField(default=False)
    about_me = models.TextField("About me")
    emergency_contact = PhoneNumberField(null=False, blank=False)
    activity_pref = models.ManyToManyField(Activity)


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Full Name", max_length=1024)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField("Gender", max_length=1, choices=GENDER_CHOICES)
    pet_animal_type = models.CharField("Animal Species", max_length=1024)
    pet_breed = models.CharField("Pet Breed", max_length=1024)
    birthday = models.DateField(null=True, blank=True)
    about_me = models.TextField("About me")
    emergency_contact = PhoneNumberField(null=False, blank=False)
    activity_pref = models.ManyToManyField(Activity)


class SeniorCitizen(models.Model):
    senior_citizen_id = models.AutoField(primary_key=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Full Name", max_length=1024)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField("Gender", max_length=1, choices=GENDER_CHOICES, blank=True)
    birthday = models.DateField(null=True, blank=True)
    want_pet = models.BooleanField(default=True)
    want_child = models.BooleanField(default=True)
    about_me = models.TextField("About me", blank=True)
    emergency_contact = PhoneNumberField(null=True, blank=True)
    activity_pref = models.ManyToManyField(Activity, blank=True)


class TOPYStation(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField("Full Name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024, )
    address2 = models.CharField("Address line 2", max_length=1024, )
    zip_code = models.CharField("ZIP / Postal code", max_length=12, )
    city = models.CharField("City", max_length=1024, )
    country = CountryField()
    phone = PhoneNumberField(null=False, blank=False)


class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    senior_citizen = models.ForeignKey(SeniorCitizen, on_delete=models.CASCADE)
    initiator_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    topy_location = models.ForeignKey(TOPYStation, on_delete=models.CASCADE)
    status = models.CharField("Status", max_length=1024,)