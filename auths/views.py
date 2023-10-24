from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import ReaderRegistrationForm
from django.shortcuts import redirect

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
    context = {'role': 'Reader', 'form': form}
    return render(request, 'register.html', context)


def register_as_author(request):
    return HttpResponse('register as author')


def login_user(request):
    return HttpResponse('login user')
