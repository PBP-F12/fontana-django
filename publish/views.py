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
    # check if user.role is AUTHOR
    # if not, then return HttpResponseForbidden
    if request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    # create book form
    form = BookForm(request.POST or None)

    # if yes, check if request method is POST
    if form.is_valid() and request.method == 'POST':
        # add author field before save the book to database
        book = form.save(commit=False)
        book.author_id = request.user
        # save book to database
        book.save()

        return HttpResponseRedirect(reverse('publish:get_book_by_author'))

    # display publish form in html
    context = {'form': form}
    return render(request, 'publish_book.html', context)


@login_required(login_url=reverse_lazy('auths:login'))
def get_book_by_author(request):
    # check if user.role is AUTHOR
    # if not, then return HttpResponseForbidden
    if request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    # get author's books
    books = Book.objects.filter(author_id=request.user.id)

    # display author's books in html
    context = {'books': books}
    return render(request, 'author_books.html', context)
