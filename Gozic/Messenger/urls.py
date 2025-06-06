from django.urls import path, include
from Messenger.views import create_groupchat, search, messenger,login, get_or_create_chatroom,chat_file_upload
urlpatterns = [
    path('', messenger, name='messenger'),
    path("chat/<username>", get_or_create_chatroom, name='start-chat'),
    path('chat/room/<chatroom_name>', messenger, name='chatroom'),
    path('chat/search/<int:groupId>',search,name='search_message' ),
    path('chat/fileupload/<chatroom_name>', chat_file_upload, name="chat-file-upload"),
    path('creategroup',create_groupchat,name="createGroup")
]
