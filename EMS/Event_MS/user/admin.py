from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models
from .models import *


# Register your models here.


# class RegisterAdmin(admin.ModelAdmin):

admin.site.register(EventFood)
