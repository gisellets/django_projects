from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Cat, Type
from .forms import CatForm, TypesForm
# Create your views here.

class TypeIndexView(generic.ListView):
    model = Type

class TypeDetailView(generic.DetailView):
    model = Type

class DetailView(generic.DetailView):
    model = Cat

class TypeCreateView(generic.edit.CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy("types:index")

class TypeUpdateView(generic.edit.UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy("types:index")

class TypeDeleteView(generic.edit.DeleteView):
    model = Type
    success_url = reverse_lazy("types:index")

class CreateView(generic.edit.CreateView):
    model = Cat
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy("types:detail" , kwargs={"pk": self.object.type.id})
class UpdateView(generic.edit.UpdateView):
    model = Cat
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy("types:detail" , kwargs={"pk": self.object.type.id})

class DeleteView(generic.edit.DeleteView):
    model = Cat
    def get_success_url(self):
        return reverse_lazy("types:detail" , kwargs={"pk": self.object.type.id})
