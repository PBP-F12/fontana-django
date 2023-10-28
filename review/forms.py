from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review_text", "review_rating"]
        widgets = {
            'review_rating': forms.HiddenInput(),
        }
