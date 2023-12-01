from django.urls import path
from .views import HotelListCreateAPIView, HotelDetailAPIView, RoomListCreateAPIView, RoomDetailAPIView, BookingListCreateAPIView, BookingDetailAPIView, UserListCreateAPIView, UserDetailAPIView, ReviewListCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    
    path('hotels/', HotelListCreateAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListCreateAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking_detail'),
    path('users/', UserListCreateAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),
]
