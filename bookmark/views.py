from django.shortcuts import render, get_object_or_404
from bookmark.models import Bookmark
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from main.models import Book
from django.core import serializers

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


def get_bookmark_by_user_ajax(request):
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

    return JsonResponse({'bookmarks': json_response})
