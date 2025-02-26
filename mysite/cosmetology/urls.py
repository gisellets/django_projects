from django.urls import path

from . import views

app_name = "cosmetology"
urlpatterns = [
    # ex: /cosmetology/, show all services
    path("", views.ServicesIndexView.as_view(), name="index"),
    # ex: /cosmetology/services/5/, detail for one service
    path("service/<int:pk>/", views.ServicesDetailView.as_view(), name="Services_detail"),
    path("timeslot/<int:pk>/", views.TimeslotDetailView.as_view(), name="Timeslot_detail"),
]
