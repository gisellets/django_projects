from django.shortcuts import render
from django.views import generic

from .models import Services, Timeslot
# Create your views here.
class ServicesIndexView(generic.ListView):
    model = Services

class ServicesDetailView(generic.DetailView):
    model = Services

class TimeslotDetailView(generic.DetailView):
    model = Timeslot
