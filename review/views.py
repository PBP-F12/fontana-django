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
from django.http import JsonResponse
import json
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url=reverse_lazy('auths:login'))
def book_details(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    context = {
        'book': book,
        'userCurrent': request.user,
        'role': request.user.role,
    }
    return render(request, 'book_details.html', context)


def get_review_json(request, book_id):
    try:
        if request.user.role != 'READER' and request.user.role != 'AUTHOR' and request.user.role != 'ADMIN':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

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


@csrf_exempt
def create_review_flutter(request, book_id):

    try:
        if request.user.role != 'READER':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    if request.method == 'POST':
        data = json.loads(request.body)

        new_review = Review.objects.create(
            user_id=request.user,
            book_id=Book.objects.get(book_id=book_id),
            review_text=data['content'],
            review_rating=data['rating'],
        )

        new_review.save()

        return JsonResponse({'message': 'Review created successfully.', 'status': 200}, status=200)
    else:
        return JsonResponse({'message': 'Error creating review.', 'status': 401}, status=401)


@csrf_exempt
def get_detail_book(request, book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk=book_id)

            return JsonResponse({'message': 'Success', 'status': 200, 'book': {
                'id': book.book_id,
                'title': book.book_title,
                'image': book.book_cover_link,
                'rating': book.avg_rating,
                'description': book.description,
                'author': {
                    'username': book.author_id.username
                }
            }}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Not found.', 'status': 404}, status=404)
        except:
            return JsonResponse({'message': 'Internal server error', 'status': 500}, status=500)
    else:
        return JsonResponse({'message': 'BAD REQUEST', 'status': 400}, status=400)
