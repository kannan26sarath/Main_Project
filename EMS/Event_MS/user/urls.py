
from django.urls import path
from . import views
app_name='user'
urlpatterns = [

    path('', views.home_view, name="home"),
    path('login/',views.login_view,name="login"),
    path ('Register/',views.register_view,name='register'),
]