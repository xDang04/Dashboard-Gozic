from django.db import models
from django.conf import settings

class Request(models.Model):
    REQUEST_TYPES = [
        ('Vacation', 'Vacation'),
        ('Sick Leave', 'Sick Leave'),
        ('Work remotely', 'Work remotely'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]
    TIME_TYPES = [
        ('days', 'Days'),
        ('hours', 'Hours'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    time_type = models.CharField(max_length=10, choices=TIME_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def duration(self):
        diff = (self.end_date - self.start_date).days
        return diff if diff > 0 else 1