from django.shortcuts import render
from .models import *

# Create your views here.
def registration(request):
    # FirstName = request.POST['FirstName']
    # LastName = request.POST['LastName']
    # date_of_birth = request.POST['date_of_birth']
    # GenderName = request.POST['GenderName']
    # country = request.POST['country']
    # StateOrDistrict = request.POST['StateOrDistrict']
    # Town = request.POST['Town']
    # ZipCode = request.POST['ZipCode']
    # PhoneNumber1 = request.POST['PhoneNumber1']
    # PhoneNumber2 = request.POST['PhoneNumber2']
    # Email = request.POST['Email']
    # if BioData.objects.filter(username=FirstName).first():
    #     print('Name already exists.')
    #     return render(request, 'register.html')
    # else:
    #     return False
    return render(request, 'register.html')
    
