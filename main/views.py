from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from bookmark.models import Bookmark
from auths.models import Author
from auths.models import Reader

from .models import Book

# Create your views here.


@login_required(login_url='auth/login')
def show_main(request):
    books = Book.objects.all()

    top_books = books[0:9]
    explore_books = books[10:100]

    context = {'role': request.user.role,
               'top_books': top_books, 'explore_books': explore_books}
    return render(request, 'main.html', context)


@login_required(login_url='auth/login')
def get_book_ajax(request):
    books = Book.objects.all()
    top_books = books[0:9]
    explore_books = books[10:]

    bookmarks = Bookmark.objects.filter(user_id=request.user)
    book_ids_in_bookmark = []
    for bookmark in bookmarks:
        book_ids_in_bookmark.append(bookmark.book_id.book_id)

    top_books_json = []
    for top_book in top_books:
        top_books_json.append({
            'id': top_book.book_id,
            'cover': top_book.book_cover_link,
            'title': top_book.book_title,
            'authorUsername': top_book.author_id.username,
            'avgRating': top_book.avg_rating,
            'description': f'{top_book.description[:50]}...'
        })

    explore_books_json = []
    for explore_book in explore_books:
        if len(explore_book.book_title) > 30:
            title = f'{explore_book.book_title[0:30]}...'
        else:
            title = explore_book.book_title

        if explore_book.book_id in book_ids_in_bookmark:
            is_bookmark = True
            print('hehe')
            bookmark_id = bookmarks[book_ids_in_bookmark.index(
                explore_book.book_id)].bookmark_id
            print(bookmark_id)
        else:
            is_bookmark = False
            bookmark_id = None

        explore_books_json.append({
            'id': explore_book.book_id,
            'cover': explore_book.book_cover_link,
            'title': title,
            'authorUsername': explore_book.author_id.username,
            'isBookmarked': is_bookmark,
            'bookmarkId': bookmark_id
        })

    json_response = {
        'role': request.user.role,
        'topBooks': top_books_json,
        'exploreBooks': explore_books_json
    }

    return JsonResponse(json_response)


def get_book_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")
    
def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_author_name(request, id):
    author = Author.objects.get(pk=id)  # Using get() instead of filter()
    authorName = author.username
    return JsonResponse({"name": authorName})

def get_reader_name(request, id):
    reader = Reader.objects.get(pk=id)  # Using get() instead of filter()
    readerName = reader.username
    return JsonResponse({"name": readerName})

