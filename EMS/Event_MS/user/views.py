from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register,UserProfile
from django.shortcuts import render
from .form import register_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from users.forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    return render(request, "user/login.html")


def login_view(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        r = Register.objects.filter(unm=un, psw=pw)
        print(r)
        if (r.count() > 0):
            return render(request, "user/home.html")

            # return HttpResponse('success')
        else:
            return render(request, 'user/login.html', {'error_code': 'wrong username or password', })
        # return HttpResponse(un+' '+pw)
    else:
        return HttpResponse('hi')

def register_view (request):
    form = register_form()
    profileform = UserProfile()

    if request.method=='POST':
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    return render(request,'user/register.html', {'form': form})



# Create your views here.
