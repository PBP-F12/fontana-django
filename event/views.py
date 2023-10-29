from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .models import Event
from .forms import EventForm

# Create your views here.
@login_required(login_url=reverse_lazy('auths:login')) 
def list_event(request):
    event = Event.objects.all()
    context = {'events': event}
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
