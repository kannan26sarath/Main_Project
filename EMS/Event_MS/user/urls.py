
from django.urls import path
from . import views
app_name='user'
urlpatterns = [

    path('home/', views.home_view, name="home"),
    path('',views.login_view, name="login"),
    path('Register/', views.register_view, name='register'),
    path('Booking/', views.booking_view, name='booking'),
    path('Fooding/', views.food_view, name='fooding'),
]