from django.urls import path, include
from Messenger.views import messenger
urlpatterns = [
    path('', messenger, name='messenger'),
]
