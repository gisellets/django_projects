from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Cat, Specie
from .forms import CatForm, SpeciesForm
# Create your views here.

class IndexView(generic.ListView):
    model = Specie

class DetailView(generic.DetailView):
    model = Specie

class DetailView(generic.DetailView):
    model = Cat

class CreateView(generic.edit.CreateView):
    model = Specie
    fields = '__all__'
    success_url = reverse_lazy("cats:index")

class UpdateView(generic.edit.UpdateView):
    model = Specie
    fields = '__all__'
    success_url = reverse_lazy("cats:index")

class DeleteView(generic.edit.DeleteView):
    model = Specie
    success_url = reverse_lazy("cats:index")

class CreateView(generic.edit.CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy("species:index")

class UpdateView(generic.edit.UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy("species:index")

class DeleteView(generic.edit.DeleteView):
    model = Cat
    success_url = reverse_lazy("species:index")
