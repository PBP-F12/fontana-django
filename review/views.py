from django.shortcuts import render
from .models import Review
from django.shortcuts import get_object_or_404
from main.models import Book
from django.http import HttpResponse
from django.core import serializers
from .forms import ReviewForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def book_details(request, book_id):
    print(book_id)
    book = get_object_or_404(Book, book_id=book_id)
    return render(request, 'book_details.html', {'book': book})

def show_mainbruh(request):
    return render(request, 'mainbruh.html')

def get_review_json(request, book_title):
    book = get_object_or_404(Book, book_title=book_title)
    reviews = Review.objects.filter(book_id=book)
    return HttpResponse(serializers.serialize('json', reviews), content_type='application/json')

def create_review(request, book_title):
    book = get_object_or_404(Book, book_title=book_title)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Assign the user and book to the form before saving
            form.instance.user_id = request.user
            form.instance.book_id = book
            form.save()
            # Redirect to the book detail page or any other page you prefer
            return HttpResponseRedirect(reverse('review:book_details', args=[book_title]))
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'add_review.html', context)

# Create your views here.
