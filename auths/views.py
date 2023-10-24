from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def register_as_reader(request):
    return HttpResponse('register as reader')


def register_as_author(request):
    return HttpResponse('register as author')


def login_user(request):
    return HttpResponse('login user')
