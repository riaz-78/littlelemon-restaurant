from django.urls import path
from . import views

app_name='restaurant'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('book/',views.book_view,name='book'),
    path('api/menu/',views.menu_api,name='menu_api'),
    path('api/bookings/',views.booking_api,name='booking_api'),
]
