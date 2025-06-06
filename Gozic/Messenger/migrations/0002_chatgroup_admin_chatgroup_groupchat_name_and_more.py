# Generated by Django 5.2.1 on 2025-06-02 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groupchats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='groupchat_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
