from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room, Booking, Review

def view_hotels(request, ):
    hotels = Hotel.objects.all()
    print(hotels[0], 'blyad')
    print(request.get_full_path(), 'blyad')
    return render(request, 'home_page.html', {'hotels': hotels, 'test': 'test'})

def hotel_detail(request, item_id):
    print(item_id, 'blyat2')
    hotel = Hotel.objects.get(id=item_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

def view_rooms(request, hotel_id):
    rooms = Room.objects.filter(hotel_id=hotel_id)
    return render(request, 'view_rooms.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'room_detail.html', {'room': room})

@login_required
def book_room(request, room_id):
    if request.method == 'POST':
        room = Room.objects.get(id=room_id)
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']

    return render(request, 'book_room.html', {'room': room})

@login_required
def view_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    return render(request, 'view_bookings.html', {'bookings': bookings})

@login_required
def leave_review(request, hotel_id):
    if request.method == 'POST':
        hotel = Hotel.objects.get(id=hotel_id)
        comment = request.POST['comment']
        rating = request.POST['rating']

    return render(request, 'leave_review.html', {'hotel': hotel})


def user_profile(request):
    return render(request, 'user_profile.html')

@login_required
def manage_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'manage_hotels.html', {'hotels': hotels})

@login_required
def manage_hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    return render(request, 'manage_hotel_detail.html', {'hotel': hotel})

@login_required
def manage_rooms(request, hotel_id):
    rooms = Room.objects.filter(hotel_id=hotel_id)
    return render(request, 'manage_rooms.html', {'rooms': rooms})

@login_required
def add_room(request, hotel_id):
    if request.method == 'POST':
        return render(request, 'add_room.html')

@login_required
def manage_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'manage_bookings.html', {'bookings': bookings})

@login_required
def modify_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        return render(request, 'modify_booking.html', {'booking': booking})

@login_required
def analytics(request):
    return render(request, 'analytics.html')

