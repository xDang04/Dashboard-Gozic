from django.db import models
from Account.models import Account


class LeaveType(models.TextChoices):
    VACATION = 'vacation', 'Vacation'
    SICK = 'sick', 'Sick Leave'
    REMOTE = 'remote', 'Work Remotely'

class RequestMode(models.TextChoices):
    DAYS = 'days', 'Days'
    HOURS = 'hours', 'Hours'

class TimeOffRequest(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=10, choices=LeaveType.choices)
    request_mode = models.CharField(max_length=5, choices=RequestMode.choices)
    
    # days
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    # hours
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.leave_type} ({self.request_mode})"
