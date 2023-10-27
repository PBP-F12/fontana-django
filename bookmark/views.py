from django.shortcuts import render
from bookmark.models import Bookmark
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from main.models import Book

def add_bookmark(request, book_id):
    # cek apakah sudah pernah di bookmark
    
    # simpan bookmark
    book_bookmarked = Book.objects.get(pk=book_id)
    new_bookmark = Bookmark(user_id=request.user, book_id=book_bookmarked)
    new_bookmark.save()

    return HttpResponse('add bookmark success')



def delete_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, bookmark_id=bookmark_id)
    bookmark.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_bookmark_by_user(request):
    bookmark = Bookmark.objects.filter(user_id=request.user)
    context = {'bookmarks': bookmark}

    return render(request, 'my_bookmark.html', context)
# Create your views here.
