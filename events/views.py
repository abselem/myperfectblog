from django.shortcuts import render
from django.urls.resolvers import _route_to_regex
from .models import Event

def home(request):
    events = Event.objects
    return render(request, 'events/home.html', {'events':events})
