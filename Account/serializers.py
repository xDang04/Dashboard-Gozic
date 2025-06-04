from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(required=False)
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'phone', 'birthday', 'age', 'position', 'location', 'company', 'skype']
        
class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Account
        fields = ['username' , 'password']
        fields = ['username' , 'password']

