from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
        # ex: /polls/
        path('', views.IndexView.as_view(), name='index'),
        # ex: /polls/5
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
