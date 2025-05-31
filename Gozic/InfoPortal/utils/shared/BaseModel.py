from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    create_by = models.CharField(max_length=100, blank=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
