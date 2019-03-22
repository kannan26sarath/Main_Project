from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from .models import UserProfile



class register_form (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user

    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ['Location', 'age']


