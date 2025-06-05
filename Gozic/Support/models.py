from django.db import models
from Account.models import Account
# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Support(models.Model):
    content = models.TextField(max_length=500)
    field = models.ManyToManyField(Field,related_name="support")
    author = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="support")