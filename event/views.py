from django.shortcuts import render
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
def publish_event(request):
    if request.user.role != 'ADMIN':
        return HttpResponseForbidden('FORBIDDEN')

    form = EventForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        forum = form.save(commit=False)
        # forum.book_id = request.user
        forum.save()

        return HttpResponseRedirect(reverse('event:list_event'))

    context = {'form': form}
    return render(request, "create_event.html", context)

@login_required(login_url=reverse_lazy('auths:login'))
def list_event_ajax(request):
    if request.user.role != 'ADMIN':
        return HttpResponseForbidden('FORBIDDEN')

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
