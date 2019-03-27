from django.db import models
from django.contrib.auth.models import User



# Create your models here.
GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
EVENT_CHOICES = (('wedding', 'Wedding'), ('engagement', 'engagement'))
#RELIGION_CHOICES = (('hindu', 'Hindu'), ('christian', 'Christian'),('muslim', 'Muslim'),)

# class Register(models.Model):
#     unm=models.CharField(max_length=100)
#     psw=models.CharField(max_length=100)

class RegUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    location = models.CharField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=12, blank=True, null=False)




    def __str__(self):
        return self.user.username

class EventBook(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    #booking_id = models.IntegerField(blank=True, null=False)
    event_type= models.CharField(max_length=10, choices=EVENT_CHOICES)
    event_location = models.CharField(max_length=12, blank=True, null=False)
    no_of_guest = models.IntegerField(max_length=12, blank=True, null=False)
    event_time = models.TimeField(max_length=12, blank=True, null=False)
    event_date = models.DateField(auto_now=False, auto_now_add=False)






    def __str__(self):
        return self.user.username


class EventFood(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    veg = models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)




    def __str__(self):
        return self.user.username

# Create your models here.
