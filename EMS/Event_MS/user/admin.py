from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models

from .models import Register
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['unm','psw']
admin.site.register(Register,RegisterAdmin)
