from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Cat
from .forms import CatForm
# Create your views here.

class IndexView(generic.ListView):
    model = Cat

class DetailView(generic.DetailView):
    model = Cat

class CreateView(generic.edit.CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy("cats:index")

class UpdateView(generic.edit.UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy("cats:index")

class DeleteView(generic.edit.DeleteView):
    model = Cat
    success_url = reverse_lazy("cats:index")
