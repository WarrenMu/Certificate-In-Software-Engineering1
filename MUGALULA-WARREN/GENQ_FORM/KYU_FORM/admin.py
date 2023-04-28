from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(BioData)
admin.site.register(Location)
admin.site.register(ContactAndAddress)
