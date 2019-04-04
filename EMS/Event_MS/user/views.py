from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import RegUser, Manufacturer
from django.shortcuts import render
from django.views import generic
from .form import register_form, RegUserForm, BookForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from users.forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    return render(request, "user/home.html")


def login_view(request):
    if request.method == 'POST':
         un = request.POST['username']
         pw = request.POST['password']
         user=authenticate(request,username=un,password=pw)
         if user:
             return render(request, "user/home.html")
         else:
             messages.error(request, 'Invalid credinals !')
             return redirect('user:login')
    else:
        return render(request, "user/login.html")
        # r = Register.objects.filter(unm=un, psw=pw)
        # print(r)
        # if (r.count() > 0):
        #     return render(request, "user/home.html")
        #
        #     # return HttpResponse('success')
        # else:
        #     return render(request, 'user/login.html', {'error_code': 'wrong username or password', })
        # # return HttpResponse(un+' '+pw)



def register_view (request):
    form = register_form()
    profileform = RegUserForm()

    if request.method == 'POST':
        form = register_form(request.POST)
        profileform = RegUserForm(request.POST)
        if form.is_valid() and profileform.is_valid():
           user= form.save()
           print(user)
           reg = profileform.save(commit=False)
           reg.user = user
           reg.save()
           return render(request, "user/login.html")
    return render(request,'user/register.html', {'form': form, 'pform': profileform})


def booking_view(request):
    #form = register_form()
    evetbookform = BookForm()

    if request.method == 'POST':
        #form = register_form(request.POST)
        evetbookform = BookForm(request.POST)
        if evetbookform.is_valid():
           #user= form.save()
           #print(user)
           book = evetbookform.save(commit=False)
           #book.user = user
           book.save()
           #return render(request, "user/login.html")
    return render(request,'user/book_event.html', { 'pform': evetbookform})


# def food_view(request):
#     #form = register_form()
#     foodbookform = FoodForm()
#
#     if request.method == 'POST':
#
#         foodbookform = FoodForm(request.POST)
#         if foodbookform.is_valid():
#
#
#            food = foodbookform.save(commit=False)
#
#            food.save()
#
#     return render(request,'user/catering.html', { 'pform': foodbookform})
# Create your views here.



class IndexView(generic.ListView):
    template_name = 'user/decoration.html'
    print("hi")
    context_object_name = 'all_manufacturers'
    print(context_object_name)

    def get_queryset(self):
        return Manufacturer.objects.all()

class DeatailsView(generic.DetailView):
    model = Manufacturer
    template_name = 'user/detail.html'

class ManufactureCreate(CreateView):
    model = Manufacturer
    fields = ['design','stage_name','stage_price']


class ManufactureUpdate(UpdateView):
    model = Manufacturer
    fields = ['design','stage_name','stage_price' ]

class ManufactureDelete(DeleteView):
    model = Manufacturer
    success_url = reverse_lazy('user:decoration')




def check_view(request):
    post = Manufacturer.objects.all()
    print('hi')
    context = {
    'post': post
    }
    print(post)
    return render(request, 'user/decoration.html', context)

def sample_view(request):
    return render(request, "user/sample.html")







