from django.urls import path
from . import views

app_name='profile'

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('vacation/', views.request_list, name='myvacation'),
    path('add-request/', views.add_request_view, name='add_request'),
    path('settings/', views.settings, name='settings'),

]