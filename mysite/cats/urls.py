from django.urls import path

from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.TypeIndexView.as_view(), name='index'),
    path('types/<int:pk>/', views.TypeDetailView.as_view(), name = 'detail'),
    path('types/<int:pk>/add/', views.CreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('types/add/', views.TypeCreateView.as_view(), name='add'),
    path('types/update/<int:pk>/',views.TypeUpdateView.as_view(), name='update'),
    path('types/delete/<int:pk>/',views.TypeDeleteView.as_view(), name='delete'),

]
