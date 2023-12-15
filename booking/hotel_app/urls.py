from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.view_hotels, name='view_hotels'),
    path('hotel/', views.hotel_detail, name='hotel_detail'),
    path('hotel/rooms/', views.view_rooms, name='view_rooms'),
    path('room/', views.room_detail, name='room_detail'),
    path('room/book/', views.book_room, name='book_room'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('leave_review/', views.leave_review, name='leave_review'),
    path('user/profile/', views.user_profile, name='user_profile'),
]
