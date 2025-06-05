from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from InfoPortal.utils.shared.BaseModel import BaseModel
from Account.models import Account
# Create your models here.
class Folder(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    user = models.ManyToManyField(Account,related_name="folders")
    def __str__(self):
        return self.name
    
class Page(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    folder = models.ManyToManyField(Folder, related_name='pages')
    content = RichTextUploadingField()

    def __str__(self):
        return self.name