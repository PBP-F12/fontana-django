from django.shortcuts import render, get_object_or_404
from bookmark.models import Bookmark
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from main.models import Book
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def add_bookmark(request, book_id):

    # simpan bookmark
    book_bookmarked = Book.objects.get(pk=book_id)

    # # cek apakah sudah pernah di bookmark
    # bookmark = Bookmark.objects.filter(
    #     book_id=book_bookmarked, user_id=request.user)
    # if len(bookmark) > 0:
    #     return JsonResponse({'msg': 'Failed.'}, status=400)

    # simpan bookmark
    print('hi')
    new_bookmark = Bookmark(user_id=request.user, book_id=book_bookmarked)
    new_bookmark.save()

    return JsonResponse({'msg': 'Success!', 'bookmarkId': new_bookmark.bookmark_id})


def delete_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, bookmark_id=bookmark_id)
    bookmark.delete()
    return JsonResponse({'msg': 'Success!'})


def delete_bookmark_by_book_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    bookmark = Bookmark.objects.get(user_id=request.user, book_id=book)

    bookmark.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


def get_bookmark_by_user(request):
    bookmark = Bookmark.objects.filter(user_id=request.user)
    context = {'bookmarks': bookmark, 'role': request.user.role}

    return render(request, 'my_bookmark.html', context)

@csrf_exempt
def get_bookmark_by_user_ajax(request):
    try:
        if request.user.role != 'READER':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    if request.method == 'GET':
        print(request.user)
        bookmarks = Bookmark.objects.filter(user_id=request.user)

        json_response = []

        for bookmark in bookmarks:
            json_response.append({
                'bookmarkId': bookmark.bookmark_id,
                'bookId': bookmark.book_id.book_id,
                'bookCover': bookmark.book_id.book_cover_link,
                'bookTitle': bookmark.book_id.book_title,
                'authorUsername': bookmark.book_id.author_id.username
            })

        return JsonResponse({'bookmarks': json_response, 'status': 200}, status=200)
    else:
        return JsonResponse({
            'message': 'BAD REQUEST'
        }, status=400)

@csrf_exempt
def add_bookmark_ajax(request, book_id):
    try:
        if request.user.role != 'READER':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=book_id)

            new_bookmark = Bookmark(user_id=request.user, book_id=book)
            new_bookmark.save()

            return JsonResponse({'message': 'success', 'status': 200}, status=200)
        except ObjectDoesNotExist:
            return JsonReponse({'message': 'Book not found.', 'status': 404}, status=404)
    else:
        return JsonResponse({
            'message': 'BAD REQUEST',
            'status': 400
        }, status=400)

@csrf_exempt
def delete_bookmark_by_book_id_ajax(request, book_id):
    try:
        if request.user.role != 'READER':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    if request.method == 'DELETE':
        try:
            book = Book.objects.get(pk=book_id)

            user_bookmarks = Bookmark.objects.filter(user_id=request.user, book_id=book)

            if user_bookmarks.count() == 0:
                return JsonResponse({'message': 'bookmark not found', 'status': 404}, status=404)
            elif user_bookmarks.count() > 0:
                return JsonResponse({'message': 'bookmarks is more than one.', 'status': 500}, status=500)
            
            user_bookmarks[0].delete()

            return JsonResponse({'message': 'success', 'status': 200}, status=200)
        except ObjectDoesNotExist:
            return JsonReponse({'message': 'Book not found.', 'status': 404}, status=404)

    else:
        return JsonResponse({
            'message': 'BAD REQUEST',
            'status': 400
        }, status=400)