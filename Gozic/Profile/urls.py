from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_projects_view, name='profile_project'),
    path('vacations', views.vacation, name='vacation'),
    path('request-add', views.request_time_off_view, name='request_time_off'),
]