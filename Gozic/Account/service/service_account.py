from ..models import Account
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from ..serializers import AccountSerializer
from rest_framework import status
from rest_framework.response import Response

def get_all_account():
    return Account.objects.all()

def get_all_account_by_id(pk):
    return get_object_or_404(Account , pk = pk)

def create_account(validated_data):
    password = validated_data.pop('password')
    user = Account(**validated_data)
    user.set_password(password)
    user.save ()
    return user
def update_account(pk, data):
    try:
        account = Account.objects.get(pk=pk)
        for attr, value in data.items():
            setattr(account, attr, value)
        account.save()
        return account
    except Account.DoesNotExist:
        return None
    
def delete_account(account):
    account.delete()
    
def login_account(data):
    username = data.get('username')
    password = data.get('password')
    
    user = authenticate(username = username , password = password)
    if user is not None :
        serializers = AccountSerializer(user)
        return Response({"messang":"Đăng nhập thất bại"} , status = status.HTTP_200_OK)
    else:
        return Response({"messang":"Đăng nhập thất bại"},status=status.HTTP_401_UNAUTHORIZED)
    

    