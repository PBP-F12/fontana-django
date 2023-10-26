from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Book

# Create your views here.


@login_required(login_url='auth/login')
def show_main(request):
    if request.user == 'AUTHOR':
        books = Book.objects.filter(author_id=request.user)
    else:
        books = Book.objects.all()

    top_books = books[0:9]
    explore_books = books[10:100]

    context = {'role': request.user.role,
               'top_books': top_books, 'explore_books': explore_books}
    return render(request, 'main.html', context)
