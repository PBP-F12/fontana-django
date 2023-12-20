import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, JsonResponse
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

@csrf_exempt
def publish_book_flutter(request):
    try:
        if request.user.role != 'AUTHOR':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    if request.method == 'POST':
        
        data = json.loads(request.body)
        new_book = Book.objects.create(
            author_id = request.user,
            book_title = data["book_title"],
            description = data["description"],
            book_cover_link = data["book_cover_link"]
        )

        new_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def get_book_by_author_json_flutter(request):
    # Check if user.role is AUTHOR, return FORBIDDEN if not
    try:
        if request.user.role != 'AUTHOR':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    
    # Get author's books
    books = Book.objects.filter(author_id=request.user.id)
    booksJson = serializers.serialize("json", books)

    return JsonResponse({"status": "success", "books" : booksJson}, status=200)
    