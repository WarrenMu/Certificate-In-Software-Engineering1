from django.shortcuts import render
from .models import *

# Create your views here.
def registration(request):

    return render(request, 'register.html')
    
