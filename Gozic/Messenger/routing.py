from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('messenger/ws/chatroom/<str:chatroom_name>', consumers.ChatRoomConsumer.as_asgi()),
]