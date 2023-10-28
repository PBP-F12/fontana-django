from django import forms
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_name", "description", "poster_link", "location", "event_date", "book_id"]
        widgets = {
            'event_date': DateInput()
        }