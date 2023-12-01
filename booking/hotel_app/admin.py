from django.contrib import admin
from .models import Hotel, Room, Booking, Review

# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass