from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import AuthorRegistrationForm, ReaderRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.


def register_as_reader(request):
    form = ReaderRegistrationForm()

    if request.method == "POST":
        form = ReaderRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been successfully created!')
            return redirect('auths:login')
    context = {
        'role': 'Reader',
        'form': form,
        'register_as_another_role_href': '/auth/register/author',
        'another_role': 'Author'
    }
    return render(request, 'register.html', context)


def register_as_author(request):
    form = AuthorRegistrationForm()

    if request.method == "POST":
        form = AuthorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been successfully created!')
            return redirect('auths:login')
    context = {'role': 'Author', 'form': form, 'register_as_another_role_href': '/auth/register/reader',
               'another_role': 'Reader'}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(
                request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
