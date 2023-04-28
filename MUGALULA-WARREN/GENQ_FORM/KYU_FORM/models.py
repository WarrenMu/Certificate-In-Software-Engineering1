from django.db import models

# Create your models here. 

#Bio Data
class BioData(models.Model):
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    def __str__(self):
        return str(self.date_of_birth)
    Male = 'M'
    Female = 'F'
    GenderChoices = [(Male, 'Male'), (Female, 'Female')]
    GenderName = models.CharField(max_length=2, choices=GenderChoices)
    def __str__(self):
        return self.GenderName()

#Location
class Location(models.Model):
    country = models.CharField(max_length=25)
    StateOrDistrict = models.CharField(max_length=25)
    Town = models.CharField(max_length=25)
    ZipCode = models.IntegerField(max_length=6)
    
#Contacts and Address
class ContactAndAddress(models.Model):
    PhoneNumber1 = models.IntegerField(max_length=20)
    PhoneNumber2 = models.IntegerField(max_length=20)
    Email = models.CharField(max_length=20)
    
    
    
    
    