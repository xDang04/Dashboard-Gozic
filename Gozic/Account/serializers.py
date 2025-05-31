from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(required=False)
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'phone', 'birthday', 'position', 'location', 'company', 'skype']