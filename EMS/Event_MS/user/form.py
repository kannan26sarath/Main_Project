from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from .models import RegUser, EventBook ,EventFood


class register_form (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            "first_name": "Name"
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user





class RegUserForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = ['address', 'gender', 'location', 'phone']


class BookForm(forms.ModelForm):
    class Meta:
        widgets = {
                    'event_date': forms.DateInput(attrs={'class': 'datepicker'}),
                }

        model = EventBook
        fields = ['event_type', 'event_location', "no_of_guest",'event_time','event_date']
        labels = {
             "event_type": "Event Type", "event_location": "venue", "no_of_guest": "No Of Guest","event_date":"Event Date", "event_date": "Date Of Event"
        }


    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user

class FoodForm(forms.ModelForm):

    class Meta:

        model = EventFood
        fields = '__all__'
        labels = {
            "breakfast": "BreakFast","lunch": "Lunch","tea_snack": "Tea & Snacks","supper": "Supper",
        }


    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user




