from django.db import models

# Create your models here.
from django.db import models
from Account.models import Account

class Vacation(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sick_leave = models.IntegerField(default=0)
    work_remotely = models.IntegerField(default=0)
    year = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def total_vacations(self):
        return self.sick_leave + self.work_remotely

    def __str__(self):
        return self.account.username