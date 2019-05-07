from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




# Create your models here.
GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
EVENT_CHOICES = (('wedding', 'Wedding'), ('engagement', 'engagement'))
FOOD_CHOICES =(('veg', 'Vegetarian'),('nonveg', 'Non-vegetarian & Vegetarian'))


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


# class EventFood(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # breakfast = models.BooleanField(default=False)
#     # lunch = models.BooleanField(default=False)
#     # tea_snack = models.BooleanField(default=False)
#     # supper = models.BooleanField(default=False)
#
#     food_type = models.CharField(max_length=10, choices=FOOD_CHOICES)
#     breakfast_type = models.CharField(max_length=10, choices=FOOD_CHOICES)
#     lunch_type = models.CharField(max_length=10, choices=FOOD_CHOICES)
#     tea_snack_type = models.CharField(max_length=10, choices=FOOD_CHOICES)
#     supper_type = models.CharField(max_length=10, choices=FOOD_CHOICES)
#
#
#
#
#
#     def __str__(self):
#         return self.user.username
#
# class  Breakfast_menu(models.Model):
#     brekfast_item = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.user.brekfast_item


# Create your models here.
class Manufacturer(models.Model):
    stage_name = models.CharField(max_length=250)
    #country = models.CharField(max_length=150)
    #estblshd_yr = models.IntegerField(max_length=5)
    design = models.FileField()
    stage_price = models.IntegerField(max_length=12, blank=True, null=False)
    s_description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.stage_name

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'pk':self.pk})


class Breakfast(models.Model):
    B_name = models.CharField(max_length=250)
    B_img = models.FileField()
    B_price = models.IntegerField(max_length=12, blank=True, null=False)
    B_description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.B_name

    def get_absolute_url(self):
        return reverse('user:Bdetail', kwargs={'pk':self.pk})
class Lunch(models.Model):
    L_name = models.CharField(max_length=250)
    L_img = models.FileField()
    L_price = models.IntegerField(max_length=12, blank=True, null=False)
    L_description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.L_name

    def get_absolute_url(self):
        return reverse('user:Ldetail', kwargs={'pk':self.pk})
class Tea(models.Model):
    T_name = models.CharField(max_length=250)
    T_img = models.FileField()
    T_price = models.IntegerField(max_length=12, blank=True, null=False)
    T_description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.T_name

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'pk':self.pk})
class Supper(models.Model):
    S_name = models.CharField(max_length=250)
    S_img = models.FileField()
    S_price = models.IntegerField(max_length=12, blank=True, null=False)
    S_description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.S_name

    def get_absolute_url(self):

        return reverse('user:detail', kwargs={'pk':self.pk})
class Cart(models.Model):
    #user_id = models.IntegerField(max_length=12, blank=True, null=False)Manufacturer
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    event_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.event_date)


class Services(models.Model):

    service_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.service_name)


class Subservices(models.Model):
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    #sub_sname = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    design = models.FileField(default='ab.jpg')
    price = models.IntegerField(max_length=12, blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    def __str__(self):
        return str(self.name)

class Booknow(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    event_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.event_date)
class Fdtypes(models.Model):
    sub_service_id = models.ForeignKey(Subservices, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    design = models.FileField()
    price = models.IntegerField(max_length=12, blank=True, null=False)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

class Venue(models.Model):
    V_name = models.CharField(max_length=250)
    V_img = models.FileField()
    V_price = models.IntegerField(max_length=12, blank=True, null=False)
    V_description = models.TextField(blank=True, null=False)
    V_location = models.CharField(max_length=250)

    def __str__(self):
        return self.V_name

    def get_absolute_url(self):
        return reverse('user:Vdetail', kwargs={'pk': self.pk})
class Contactus(models.Model):
    C_name = models.CharField(max_length=250)
    C_email = models.CharField(max_length=250)
    C_message= models.TextField(blank=True,null=False)
    def __str__(self):
        return self.C_email
class Feedback(models.Model):
    F_name = models.CharField(max_length=250)
    F_email = models.CharField(max_length=250)
    F_review= models.TextField(blank=True,null=False)
    F_OE = models.CharField(max_length=250)
    F_TR = models.CharField(max_length=250)
    F_OS = models.CharField(max_length=250)
    F_satisfaction = models.CharField(max_length=250)
    F_rating = models.TextField(max_length=250)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.F_name

