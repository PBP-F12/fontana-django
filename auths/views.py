from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.core import serializers

from .models import Reader, User
from .forms import AuthorRegistrationForm, ProfilePictureForm, ReaderRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from os import path
import os

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
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Status login sukses.
                    return JsonResponse({
                        'userId': user.id,
                        "username": user.username,
                        "message": "Login sukses!",
                        'role': user.role,
                        "status": 200,
                        # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                    }, status=200)
                else:
                    return JsonResponse({
                        "status": 401,
                        "message": "Login gagal, akun dinonaktifkan."
                    }, status=401)

            else:
                return JsonResponse({
                    "message": "Login gagal, periksa kembali email atau kata sandi.",
                    "status": 404,
                }, status=404)
        except:
            return JsonResponse({'message': 'No payload provided', 'status': 400}, status=400)
    else:
        return JsonResponse({
            "status": 400,
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
                "message": "Username is already exist",
                'status': 409,
            }, status=409)
        except ObjectDoesNotExist:
            form = ReaderRegistrationForm(request.POST)
            if form.is_valid():
                form.save()

                return JsonResponse({
                    "message": "Register success",
                    'status': 200,
                }, status=200)

            else:
                return JsonResponse({"message": "Form is not valid.", 'status': 400, }, status=400)
        except Exception as e:
            print(f'Error: {e}')
            return JsonResponse({
                "message": "Internal Server Error.",
                'status': 500,
            }, status=500)
    else:
        return JsonResponse({
            "message": "Bad request",
            'status': 400,
        }, status=400)


@csrf_exempt
def register_as_author_api(request):
    if request.method == 'POST':
        username = request.POST['username']

        # check if user is already available
        try:
            user = User.objects.get(username=username)
            return JsonResponse({
                "message": "Username is already exist",
                'status': 409,
            }, status=409)
        except ObjectDoesNotExist:
            form = AuthorRegistrationForm(request.POST)
            if form.is_valid():
                form.save()

                return JsonResponse({
                    "message": "Register success",
                    'status': 200,
                }, status=200)

            else:
                return JsonResponse({"message": "Form is not valid.", 'status': 400, }, status=400)
        except Exception as e:
            print(f'Error: {e}')
            return JsonResponse({
                "message": "Internal Server Error.",
                'status': 500,
            }, status=500)
    else:
        return JsonResponse({
            "message": "Bad request",
            'status': 400,
        }, status=400)


@csrf_exempt
def logout_user_api(request):
    username = request.user.username

    try:
        logout(request)
        return JsonResponse({
            "username": username,
            "status": 200,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
            "status": 401,
            "message": "Logout gagal."
        }, status=401)


@csrf_exempt
def get_user_data(request):
    try:
        if request.user.role != 'READER' and request.user.role != 'AUTHOR':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    if request.method == 'GET':
        try:
            user = request.user

            return JsonResponse({'message': 'Success!', 'status': 200, "user": {
                "username": user.username,
                "fullName": user.full_name,
                "role": user.role
            }}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'User not found.', 'status': 404}, status=404)
        except:
            return JsonResponse({'message': 'Internal Server Error.', 'status': 500}, status=500)
    else:
        return JsonResponse({'message': 'Bad Request.', 'status': 400}, status=400)


@csrf_exempt
def upload_profile_picture(request):
    if request.method == 'POST':
        try:
            if request.user.role != 'READER' and request.user.role != 'AUTHOR' and request.user.role != 'ADMIN':
                return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
        except:
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

        if request.FILES:
            profile_picture = request.FILES['profile_picture']

            user = User.objects.get(pk=request.user.id)
            user.profile_picture = profile_picture
            user.save()
            print(user.username)
            return JsonResponse({'message': 'success'}, status=200)

        else:
            return JsonResponse({'message': 'Bad Request. No file received.', 'status': 400}, status=400)

    elif request.method == 'GET':
        user_id = request.GET.get('id')

        if not user_id:
            return JsonResponse({'message': 'Bad Request.', 'status': 400}, status=400)

        user = User.objects.get(pk=user_id)

        return FileResponse(user.profile_picture)

    else:
        return JsonResponse({'message': 'Bad Request.', 'status': 400}, status=400)
