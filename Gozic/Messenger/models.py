from django.db import models
from Account.models import Account
from PIL import Image
# Create your models here.

class ChatGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users_online = models.ManyToManyField(Account, related_name="online_in_groups", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(Account, related_name="members_groups", blank=True)
    is_group = models.BooleanField(default=True)
    groupchat_name = models.CharField(max_length=100, null=True, blank=True)
    admin = models.ForeignKey(Account, related_name='groupchats', blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(Account,on_delete=models.CASCADE) 
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return f"{self.author.username} in {self.group.name}: {self.body[:20]}"
    
    class Meta:
        ordering = ['created']
    
    @property    
    def is_image(self):
        try:
            image = Image.open(self.file) 
            image.verify()
            return True 
        except:
            return False