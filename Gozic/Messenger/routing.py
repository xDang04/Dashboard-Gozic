from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chatroom/(?P<chatroom_name>[^/]+)$', consumers.ChatRoomConsumer.as_asgi()),
]
# from django.urls import path
# from . import consumers

# websocket_urlpatterns = [
#     path('ws/chatroom/<str:chatroom_name>', consumers.ChatRoomConsumer.as_asgi()),
# ]