from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
import json
from .models import *
from django.db.models import OuterRef, Subquery

from Account.models import Account

class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        id = self.user.id
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name'] 
        self.user = Account.objects.get(pk=id)
        self.chatroom = get_object_or_404(ChatGroup, name=self.chatroom_name)
        self.chatroom_name_fix = self.chatroom_name.replace(' ','_')
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name_fix, self.channel_name
        )
        
        if self.user not in self.chatroom.users_online.all():
            self.chatroom.users_online.add(self.user)
            self.update_online_count()
        GroupMembers.objects.filter(
            group__name=self.chatroom_name,
            members=self.user
        ).update(has_new_message=False)
        self.accept()
        
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name_fix, self.channel_name
        )
        # remove and update online users
        if self.user in self.chatroom.users_online.all():
            self.chatroom.users_online.remove(self.user)
            self.update_online_count() 
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']
        
        message = GroupMessage.objects.create(
            body = body,
            author = self.user, 
            group = self.chatroom 
        )
        event = {
            'type': 'message_handler',
            'message_id': message.id,
        }
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name_fix, event
        )
        
    def update_media_dropdown(self,event):
        context = {
            'message': event['message']
        }
        if event['message'].file:
            if event['message'].is_image:
                html = render_to_string('Messenger/partials/media_dropdown.html', context=context)
            else:
                html = render_to_string('Messenger/partials/file_dropdown.html', context=context)

        self.send(text_data=html)
    
    def update_message_group(self,event):
        group_id = event['group_id']
        sender_id = event['user'].id
        GroupMembers.objects.filter(
            group_id=group_id
        ).exclude(members_id=sender_id).update(has_new_message=True)
        
        
        latest_messages = GroupMessage.objects.filter(
            group=OuterRef('pk')
        ).order_by('-created')
        group = ChatGroup.objects.filter(id=group_id).annotate(
            lastest_message=Subquery(latest_messages.values("body")[:1]),
            lastest_time=Subquery(latest_messages.values("created")[:1]),
            lastest_sender=Subquery(latest_messages.values("author__username")[:1]),
            lastest_file=Subquery(latest_messages.values("file")[:1]),
        ).first()
        context = {
            'group':group,
            'user':event['user']
        }
        if group.is_group:
            html = render_to_string('Messenger/partials/group_p.html', context=context)
        else:
            html = render_to_string('Messenger/partials/directmessage_p.html', context=context)

        self.send(text_data=html)
        
    def message_handler(self, event):
        message_id = event['message_id']
        message = GroupMessage.objects.get(id=message_id)
        context = {
            'message': message,
            'user': self.user,
            'chat_group': self.chatroom
        }
        html = render_to_string('Messenger/partials/chat_message_p.html', context=context)
        self.send(text_data=html)
        
        
    def update_online_count(self):
        online_count = self.chatroom.users_online.count()
        
        event = {
            'type': 'online_count_handler',
            'online_count': online_count
        }
        async_to_sync(self.channel_layer.group_send)(self.chatroom_name_fix, event)
        
    def online_count_handler(self, event):
        online_count = event['online_count']
        
        chat_messages = ChatGroup.objects.get(name=self.chatroom_name).chat_messages.all()
        author_ids = set([message.author.id for message in chat_messages])
        users = Account.objects.filter(id__in=author_ids)
        
        context = {
            'online_count' : online_count,
            'chat_group' : self.chatroom,
            'users': users
        }
        html = render_to_string('Messenger/partials/online_user_p.html', context)
        self.send(text_data=html) 
        
        
class OnlineStatusConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.group_name = 'online-status'
        self.group = get_object_or_404(ChatGroup, name=self.group_name)
        
        if self.user not in self.group.users_online.all():
            self.group.users_online.add(self.user)
            
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        
        self.accept()
        self.online_status()
        
        
    def disconnect(self, close_code):
        if self.user in self.group.users_online.all():
            self.group.users_online.remove(self.user)
            
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        self.online_status()
        
        
    def online_status(self):
        event = {
            'type': 'online_status_handler'
        }
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, event
        ) 
        
    def online_status_handler(self, event):
        online_users = self.group.users_online.exclude(id=self.user.id)
        public_chat_users = ChatGroup.objects.get(name='public-chat').users_online.exclude(id=self.user.id)
        
        # Explicitly get the user object to ensure it's resolved
        user = Account.objects.get(id=self.user.id)
        
        my_chats = user.chat_groups.all()
        private_chats_with_users = [chat for chat in my_chats.filter(is_private=True) if chat.users_online.exclude(id=self.user.id)]
        group_chats_with_users = [chat for chat in my_chats.filter(groupchat_name__isnull=False) if chat.users_online.exclude(id=self.user.id)]
        
        if public_chat_users or private_chats_with_users or group_chats_with_users:
            online_in_chats = True
        else:
            online_in_chats = False
        
        context = {
            'online_users': online_users,
            'online_in_chats': online_in_chats,
            'public_chat_users': public_chat_users,
            'user': self.user
        }
        html = render_to_string("a_rtchat/partials/online_status.html", context=context)
        self.send(text_data=html) 