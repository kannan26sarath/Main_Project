
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
    path('FulDecorating/',views.fulcheck_view, name='fuldecor'),


    path('FulDecorating/<int:pk>/',views.fulDeatailsView.as_view(), name='fulldetail'),
    path('<int:pk>/',views.DeatailsView.as_view(), name='detail'),

    # path('<int:pk>/', views.DeatailsView.as_view(), name="sample"),
    # path('food', views.my_view, name="sample2"),
    path('Fooding/',views.food_view, name='food'),
    path('Breakfast/',views.B_view, name='breakfast'),
    path('Lunch/',views.L_view, name='lunch'),
    path('Tea/',views.T_view, name='tea'),
    path('Supper/',views.S_view, name='supper'),
    path('Cart/', views.cart_view, name="cart"),
    path('Pay/', views.payment_view, name="payment"),
    path('Breakfast/<int:pk>/',views.BfDeatailsView.as_view(), name='Bdetail'),
    path('Lunch/<int:pk>/',views.LDeatailsView.as_view(), name='Ldetail'),
    path('Tea/<int:pk>/',views.TDeatailsView.as_view(), name='Tdetail'),
    path('Supper/<int:pk>/',views.SDeatailsView.as_view(), name='Sdetail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)