from django.shortcuts import render
from .models import Review
from django.shortcuts import get_object_or_404
from main.models import Book
from django.http import HttpResponse
from django.core import serializers
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@login_required(login_url=reverse_lazy('auths:login'))
def book_details(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    context = {
        'book': book,
        'userCurrent': request.user,
        'role': request.user.role,
    }
    return render(request, 'book_details.html', context)

@login_required(login_url=reverse_lazy('auths:login'))
def get_review_json(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    reviews = Review.objects.filter(book_id=book)
    return HttpResponse(serializers.serialize('json', reviews), content_type='application/json')

@login_required(login_url=reverse_lazy('auths:login'))
def create_review(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    
    if not request.user.is_reader:
        # Redirect the user or show an error message
        return HttpResponse(status=500)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.user_id = request.user
            form.instance.book_id = book
            form.save()
            return HttpResponseRedirect(reverse('review:book_details', args=[book_id]))
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'add_review.html', context)

@csrf_exempt
@require_http_methods(["DELETE"])
@login_required(login_url=reverse_lazy('auths:login'))
def delete_review(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    review.delete()
    return HttpResponse(status=204)
    
