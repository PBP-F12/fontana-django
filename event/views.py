import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from .models import Event
from main.models import Book
from .forms import EventForm

# Create your views here.
@login_required(login_url=reverse_lazy('auths:login')) 
def list_event(request):
    event = Event.objects.all()
    book = Book.objects.all()
    context = {'events': event, 'books' : book}
    return render(request, "list_event.html", context)


@login_required(login_url=reverse_lazy('auths:login')) 
def get_event_details(request, event_id):
    event = Event.objects.get(pk=event_id)
    context = {'event': event}
    return render(request, "event_details.html", context)


@login_required(login_url=reverse_lazy('auths:login')) 
@csrf_exempt
def publish_event(request):
    if request.user.role != 'ADMIN':
        return HttpResponseForbidden('FORBIDDEN')

    form = EventForm(request.POST or None)
    if request.method == 'POST':
        form = EventForm(request.POST or None)
        event_name = request.POST.get("event_name")
        description = request.POST.get("description")
        poster_link = request.POST.get("poster_link")
        location = request.POST.get("location")
        event_date = request.POST.get("event_date")
        book_id = request.POST.get("book_id")
        book = get_object_or_404(Book, book_id=book_id)
        
        event = Event(event_name=event_name, description=description, poster_link=poster_link, location=location, event_date=event_date, book_id=book)
        event.save()

        return HttpResponseRedirect(reverse('event:list_event'))
    else:
        form = EventForm()

    context = {'form': form}
    return render(request, "create_event.html", context)


@login_required(login_url=reverse_lazy('auths:login'))
def list_event_ajax(request):
    events = Event.objects.all()
    json_response = []

    for event in events:
        event_json = {
            'eventDetailsUrl': f'/event/{event.event_id}',
            'eventName': event.event_name,
            'posterLink': event.poster_link,
            'eventDate': event.event_date
        }

        json_response.append(event_json)

    return JsonResponse({'events': json_response})

def show_json(request):
    data = Event.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, event_id):
    data = Event.objects.filter(pk=event_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        print(data)

        try:
            book = Book.objects.get(book_id=data['book_id'])
        except ObjectDoesNotExist:
            return JsonResponse({"status": "not found"}, status=404)
        except:
            return JsonResponse({"status": "error"}, status=500)

        new_product = Event.objects.create(
            event_name = data["event_name"],
            location = data["location"],
            description = data["description"],
            poster_link = data["poster_link"],
            event_date = data["event_date"],
            book_id = book,
        )
        
        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)