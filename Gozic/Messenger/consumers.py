from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from django.shortcuts import get_object_or_404
from Messenger.models import ChatGroup, GroupMessage
import json
from django.template.loader import render_to_string
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.user = self.scope['user']
            self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
            self.chatroom = await self.get_chat_group(self.chatroom_name)
            await self.channel_layer.group_add(self.chatroom_name, self.channel_name)

            # if not await self.is_user_online(self.user):
            #     await self.add_user_online(self.user)
            #     await self.update_online_count()

            print("WebSocket connected:", self.scope['user'])
            await self.accept()
        except Exception as e:
            print("WebSocket connect error:", str(e))
    @database_sync_to_async
    def get_message(self, message_id):
        return get_object_or_404(GroupMessage, id=message_id)
    @database_sync_to_async
    def get_chat_group(self, chatroom_name):
        return get_object_or_404(ChatGroup, name=chatroom_name)
    # @database_sync_to_async
    # def get_all_user_online(self):
    #     return self.chatroom.users_online.all()
    # @database_sync_to_async
    # def is_user_online(self, user):
    #     return self.chatroom.users_online.filter(id=user.id).exists()

    async def disconnect(self, close_code):
        # Leave the chatroom group
        await self.channel_layer.group_discard(
            self.chatroom_name,
            self.channel_name
        )
        # if await self.is_user_online(self.user):
        #     await self.remove_user_online(self.user)
        #     await self.update_online_count()

    async def receive(self, text_data):
        # Broadcast the received message to the chatroom group
        text_data_json = json.loads(text_data)
        body = text_data_json['body']
        message = await self.create_message(
                group=self.chatroom,
                author=self.user,
                body=body
            )
        event = {
            'type': 'message_handle',
            'message_id': message.id  # Send the message ID to handle it in the group
        }
        await self.channel_layer.group_send(
            self.chatroom_name,
            event
        )
    @database_sync_to_async
    def create_message(self,group, author, body):
        return GroupMessage.objects.create(
            group=group,
            author=author,
            body=body
        )
    async def message_handle(self,event):
        message_id = event['message_id']
        message = await self.get_message(message_id)

        html = await sync_to_async(render_to_string)(
            'Messenger/partials/chat_message_p.html',
            {'message': message, 'user': self.user}
        )
        await self.send(text_data=html)

    # @database_sync_to_async
    # def update_online_count(self):
    #     online_count = self.chatroom.users_online.all().count()
    #     event = {
    #         'type': 'online_count_handle',
    #         'online_count': online_count,
    #     }
    #     async_to_sync(self.channel_layer.group_send)(self.chatroom_name, event)
    # async def online_count_handle(self, event):
    #     online_count = event['online_count']
    #     html = await sync_to_async(render_to_string)(
    #         'a_rtchat/partials/online_count.html',
    #         {'online_count': online_count}
    #     )
    #     await self.send(text_data=html)

    # @database_sync_to_async
    # def add_user_online(self, user):
    #     self.chatroom.users_online.add(user)

    # @database_sync_to_async
    # def remove_user_online(self, user):
    #     self.chatroom.users_online.remove(user)