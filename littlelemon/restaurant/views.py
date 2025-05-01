from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Booking
import json
from datetime import datetime

def home(request):
    return render(request, 'restaurant/index.html')

def about(request):
    return render(request, 'restaurant/about.html')

def menu(request):
    return render(request, 'restaurant/menu.html')

def book(request):
    return render(request, 'restaurant/book.html')

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            booking = Booking.objects.create(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot']
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
    else:
        bookings = Booking.objects.all()
    
    booking_data = [{
        'first_name': booking.first_name,
        'reservation_date': booking.reservation_date,
        'reservation_slot': booking.reservation_slot
    } for booking in bookings]
    
    return JsonResponse(booking_data, safe=False)
