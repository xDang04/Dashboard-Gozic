from django.urls import path, include
from Messenger.views import messenger,login
urlpatterns = [
    path('', messenger, name='messenger'),
    path('login', login, name='login'),
]
