from django.urls import path
from . import views

app_name="calendar"

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('events/add/', views.add_event, name='add_event'),
]