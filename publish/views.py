from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from main.models import Book
from .forms import BookForm
from auths.models import Author

# Create your views here.
@login_required(login_url=reverse_lazy('auths:login'))
def publish_book(request):
    # Check if user.role is AUTHOR, return FORBIDDEN if not
    if request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    # Check if request method is POST
    if request.method == 'POST':
        # Create book form
        form = BookForm(request.POST or None)
        if form.is_valid():
            # Add author field before saving the book to database
            book = form.save(commit=False)
            book.author_id = request.user
            # Save book to database
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