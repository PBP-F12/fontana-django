from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.core import serializers

from .models import Reader, User
from .forms import AuthorRegistrationForm, ReaderRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

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


def logout_user(request):
    logout(request)
    return redirect('auths:login')


def get_user_by_id(request, user_id):
    user = User.objects.filter(pk=user_id)

    return HttpResponse(serializers.serialize("json", user), content_type="application/json")


@csrf_exempt
def login_user_api(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Status login sukses.
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!"
                    # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, akun dinonaktifkan."
                }, status=401)

        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali email atau kata sandi."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Bad request"
        }, status=400)


@csrf_exempt
def register_as_reader_api(request):
    if request.method == 'POST':
        username = request.POST['username']

        # check if user is already available
        try:
            user = User.objects.get(username=username)
            return JsonResponse({
                "message": "Username is already exist"
            }, status=409)
        except ObjectDoesNotExist:
            form = ReaderRegistrationForm(request.POST)
            if form.is_valid():
                form.save()

                return JsonResponse({
                    "message": "Register success"
                }, status=200)

            else:
                return JsonResponse({"message": "Form is not valid."}, status=400)
        except Exception as e:
            print(f'Error: {e}')
            return JsonResponse({
                "message": "Internal Server Error."
            }, status=500)
    else:
        return JsonResponse({
            "message": "Bad request"
        }, status=400)
