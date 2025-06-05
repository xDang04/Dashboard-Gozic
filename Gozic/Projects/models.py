

from django.db import models
from Account.models import * 
# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("In Review", "In Review"),
        ("Done", "Done"),
        ("Backlog", "Backlog"),
    ]
    name = models.CharField(max_length=255)
    project = models.ForeignKey('Projects', on_delete=models.CASCADE, null = True , related_name='tasks')  
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    create_at = models.DateField()
    dealine = models.DateField()
    assignees = models.ManyToManyField(Account, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Backlog")

    
    def __str__(self):
        return self.name
     
class Projects(models.Model):
    STATUS_CHOICES = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("In Review", "In Review"),
        ("Done", "Done"),
        ("Backlog", "Backlog"),
    ]
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    number = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Backlog") 
    reporter = models.ForeignKey(Account , on_delete=models.CASCADE , null=True , default="bạn chưa điền tên" , related_name="project_repoter")
    assignees = models.ManyToManyField(Account, blank=True , related_name="project_assignees")
    create_at = models.DateField()
    dealine = models.DateField()
    
    def __str__(self):
        return self.name