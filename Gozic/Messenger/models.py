from django.db import models
from Account.models import Account
# Create your models here.

class ChatGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users_online = models.ManyToManyField(Account, related_name="online_in_groups", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(Account,on_delete=models.CASCADE) 
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} in {self.group.name}: {self.body[:20]}"
    
    class Meta:
        ordering = ['created']