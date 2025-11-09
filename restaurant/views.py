from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, BookingForm
from .models import MenuItem, Booking
from django.utils import timezone
from django.db import IntegrityError

def index(request):
    return render(request,'restaurant/index.html')

def menu_api(request):
    items = MenuItem.objects.all()
    data = [{'id':i.id,'name':i.name,'description':i.description,'price':str(i.price)} for i in items]
    return JsonResponse({'menu': data})

@login_required
def booking_api(request):
    date = request.GET.get('date')
    qs = Booking.objects.filter(reservation_date=date) if date else Booking.objects.all()
    data = [{'id':b.id,'user':b.user.username,'slot':b.reservation_slot} for b in qs]
    return JsonResponse({'bookings': data})

def register_view(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('restaurant:index')
    else:
        form = RegisterForm()
    return render(request,'restaurant/register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('restaurant:index')
    return render(request,'restaurant/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('restaurant:login')

@login_required
def book_view(request):
    today = timezone.localdate()
    form = BookingForm(request.POST or None, initial={'reservation_date':today})
    if request.method=='POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                booking.save()
                return redirect('restaurant:index')
            except IntegrityError:
                form.add_error(None,'Slot already booked')
    return render(request,'restaurant/booking.html',{'form':form})
