from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from user.models import *
from user import config

#from .models import RegUser, Manufacturer, Supper, Tea, Lunch, Breakfast
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
             config.uid = user.id
             print(config.uid)

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
           return redirect("user:login")
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
           return redirect("user:fuldecor")
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



# class IndexView(generic.ListView):
#     template_name = 'user/decoration.html'
#
#     context_object_name = 'all_manufacturers'
#
#
#
#
#     def get_queryset(self):
#         return Manufacturer.objects.all()

class DeatailsView(generic.DetailView):
    model = Manufacturer
    template_name = 'user/detail.html'

class fulDeatailsView(generic.DetailView):
    model = Manufacturer
    template_name = 'user/fulldetail.html'


def check_view(request):
    post = Manufacturer.objects.all()

    context = {
    'post': post
    }

    print(post)
    return render(request, 'user/decoration.html', context)
def fulcheck_view(request):
    post = Manufacturer.objects.all()

    context = {
    'post': post
    }

    print(post)
    return render(request, 'user/fulldecor.html', context)

def food_view(request):
    return render(request, "user/catering.html")

def B_view(request):
    bfast = Breakfast.objects.all()

    context = {
    'bfast': bfast
    }
    print(bfast)
    return render(request, 'user/breakfast.html', context)
class BfDeatailsView(generic.DetailView):
    model = Breakfast
    template_name = 'user/Bdetail.html'

def L_view(request):
    lfast = Lunch.objects.all()

    context = {
    'lfast': lfast
    }
    print(lfast)
    return render(request, 'user/lunch.html', context)
class LDeatailsView(generic.DetailView):
    model = Lunch
    template_name = 'user/Ldetail.html'
def T_view(request):
    tfast = Tea.objects.all()

    context = {
    'tfast': tfast
    }
    print(tfast)
    return render(request, 'user/tea&snacks.html', context)
class TDeatailsView(generic.DetailView):
    model = Tea
    template_name = 'user/TSdetail.html'
def S_view(request):
    sfast = Supper.objects.all()

    context = {
    'sfast': sfast
    }
    print(sfast)
    return render(request, 'user/supper.html', context)
class SDeatailsView(generic.DetailView):
    model = Supper
    template_name = 'user/Sdetail.html'

def cart_view(request):
    if request.method=='POST':
        if request.POST.get('cart'):
            print(config.uid)
            u_id= config.uid
            u_id = User.objects.get(id=u_id)
            service_id = request.POST.get('Did')
            service_id = Manufacturer.objects.get(id=service_id)
            event_dt= request.POST.get('EventDay')
            obj = Cart(user_id=u_id, service_id=service_id, event_date=event_dt)
            obj.save()
            return render(request, "user/home.html",{'message':'added to cart successfully'})
    else:

        return render(request, "user/home.html")

            #return HttpResponse (decor_id + event_dt + str(u_id))

def Booknow_view(request):
    if request.method=='POST':
        if request.POST.get('booknow'):
            print(config.uid)
            u_id= config.uid
            u_id = User.objects.get(id=u_id)
            service_id = request.POST.get('Did')
            service_id = Manufacturer.objects.get(id=service_id)
            event_dt= request.POST.get('EventDay')
            obj = Cart(user_id=u_id, service_id=service_id, event_date=event_dt)
            obj.save()
            return render(request, "user/home.html",{'message':'added to cart successfully'})
    else:

        return render(request, "user/home.html")
def payment_view(request):
    return render(request, "user/payment.html")


def oops_view(request):
    return render(request, "user/transport.html")



def venue_view(request):
    vfast = Venue.objects.all()

    context = {
    'vfast': vfast
    }

    print(vfast)
    return render(request, 'user/venue.html', context)
def contactus_view(request):
    if request.method=='POST':
        if request.POST.get('send'):



            c_name= request.POST.get('name')
            c_email = request.POST.get('email')
            c_message = request.POST.get('message')

            obj = Contactus(C_name=c_name, C_email=c_email, C_message=c_message)
            obj.save()
            return render(request, "user/home.html",{'message':'contact send successfully'})
    else:
        return render(request, "user/contactus.html")

def feedback_view(request):
    if request.method=='POST':
        if request.POST.get('Send Feedback'):

            u_id= config.uid
            u_id = User.objects.get(id=u_id)
            f_name = request.POST.get('name')
            f_email = request.POST.get('email')
            f_review = request.POST.get('review')
            f_OE = request.POST.get('radio')
            f_TR = request.POST.get('radio1')
            f_OS = request.POST.get('radio2')
            f_satisfaction = request.POST.get('radio3')
            f_rating = request.POST.get('rating')



            obj = Feedback(F_name=f_name, F_email=f_email, F_review=f_review,F_OE=f_OE,F_TR=f_TR,F_OS=f_OS,F_satisfaction=f_satisfaction,F_rating=f_rating,user_id=u_id)
            obj.save()
            return render(request, "user/home.html",{'message':'feed back send successfully'})
    else:

        return render(request, "user/feedback.html")