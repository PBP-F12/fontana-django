from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from main.models import Book
from .forms import BookForm

# Create your views here.
@login_required(login_url=reverse_lazy('auths:login'))
@csrf_exempt
def publish_book(request):
    # Check if user.role is AUTHOR, return FORBIDDEN if not
    if request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    # Check if request method is POST
    if request.method == 'POST':
        # Create book form
        form = BookForm(request.POST or None)
        if form.is_valid():
            book_title = request.POST.get("book_title")
            description = request.POST.get("description") 
            book_cover_link = request.POST.get("book_cover_link") 
            book_cover_file = request.POST.get("book_cover_file")
            author_id = request.user

            book = Book(author_id=author_id, book_title=book_title, description=description, book_cover_link=book_cover_link, book_cover_file=book_cover_file)
            book.save()

            return HttpResponseRedirect(reverse('publish:get_book_by_author'))
    else:
        form = BookForm()
    
    # Display publish form in HTML
    context = {'form' : form}
    return render(request, 'publish_book.html', context)

@login_required(login_url=reverse_lazy('auths:login'))
def get_book_by_author(request):
    # Check if user.role is AUTHOR, return FORBIDDEN if not
    if request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')
    
    # Get author's books
    books = Book.objects.filter(author_id=request.user.id)

    # Display author's books in HTML
    context = {'books' : books}
    return render(request, 'author_books.html', context)


@login_required(login_url=reverse_lazy('auths:login'))
def get_book_by_author_json(request):
    # Check if user.role is AUTHOR, return FORBIDDEN if not
    if request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')
    
    # Get author's books
    books = Book.objects.filter(author_id=request.user.id)

    # Create an HTTP response that contains the JSON representation of books
    return HttpResponse(serializers.serialize('json', books))