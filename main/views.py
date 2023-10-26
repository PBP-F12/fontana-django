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

    context = {'role': request.user.role, 'books': books}
    return render(request, 'main.html', context)
