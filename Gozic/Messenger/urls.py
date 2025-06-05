from django.urls import path, include
from Messenger.views import search, messenger,login, get_or_create_chatroom
urlpatterns = [
    path('', messenger, name='messenger'),
    path('login', login, name='login'),
    path("chat/<username>", get_or_create_chatroom, name='start-chat'),
    path('chat/room/<chatroom_name>', messenger, name='chatroom'),
    path('chat/search/<int:groupId>',search,name='search_message' )
]
