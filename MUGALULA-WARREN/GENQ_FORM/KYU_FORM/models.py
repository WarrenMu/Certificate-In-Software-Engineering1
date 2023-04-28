from django.db import models

# Create your models here. 

#Bio Data
class BioData(models.Model):
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    Male = 'M'
    Female = 'F'
    GenderChoices = [(Male, 'Male'), (Female, 'Female')]
    GenderName = models.CharField(max_length=2, choices=GenderChoices)

#Location
class Location(models.Model):
    country = models.CharField(max_length=25)
    StateOrDistrict = models.CharField(max_length=25)
    Town = models.CharField(max_length=25)
    ZipCode = models.IntegerField()
    
#Contacts and Address
class ContactAndAddress(models.Model):
    PhoneNumber1 = models.IntegerField()
    PhoneNumber2 = models.IntegerField()
    Email = models.CharField(max_length=20)
    
    
    
    
    