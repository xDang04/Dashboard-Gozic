from django.db import models



class Event(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    priority = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)
    repeat = models.BooleanField(default=False)
    def __str__(self):
        return self.name