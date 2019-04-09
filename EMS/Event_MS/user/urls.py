
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='user'
urlpatterns = [

    path('home/', views.home_view, name="home"),
    path('',views.login_view, name="login"),
    path('Register/', views.register_view, name='register'),
    path('Booking/', views.booking_view, name='booking'),
    # path('Fooding/', views.food_view, name='fooding'),
    #path('<int:pk>/',views.DeatailsView.as_view(), name='detail'),
    path('Decorating/',views.check_view, name='decor'),
    #path('Sdetail/',views.DeatailsView.as_view(), name='details'),
    path('<int:pk>/',views.DeatailsView.as_view(), name='detail'),

    path('<int:pk>/', views.DeatailsView.as_view(), name="sample"),
    # path('Detail', views.sam2_view, name="sample2"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)