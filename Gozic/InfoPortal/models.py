from django.db import models
from InfoPortal.utils.shared.BaseModel import BaseModel
# Create your models here.
class Folder(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Page(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='pages')
    content = models.TextField()

    def __str__(self):
        return self.name