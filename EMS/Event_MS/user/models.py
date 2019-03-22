from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    unm=models.CharField(max_length=100)
    psw=models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Location = models.CharField(max_length = 40)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username


# Create your models here.
