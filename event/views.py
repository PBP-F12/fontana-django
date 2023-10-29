from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from yaml import serialize
from django.views.decorators.csrf import csrf_exempt

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
