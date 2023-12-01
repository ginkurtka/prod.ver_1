from django import forms
from .models import Booking, Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(available=True)

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date:
            if check_in_date >= check_out_date:
                raise forms.ValidationError("Дата выезда должна быть после даты заезда.")

            room = cleaned_data.get('room')
            if room:
                bookings = Booking.objects.filter(room=room, deleted=False)
                for booking in bookings:
                    if check_in_date <= booking.check_out_date and check_out_date >= booking.check_in_date:
                        raise forms.ValidationError("Эта комната уже забронирована на выбранные даты.")
        return cleaned_data