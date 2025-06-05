from django.urls import path, include
from Support.views import add_support
urlpatterns = [
    path('', add_support, name='add_support'),
]
