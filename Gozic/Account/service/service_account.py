from ..models import Account
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from ..serializers import AccountSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError

def get_all_account():
    return Account.objects.all()

def get_all_account_by_id(pk):
    return get_object_or_404(Account , pk = pk)

def create_account(validated_data):
    email = validated_data.get('email')
    password = validated_data.get('password')
    username = validated_data.get('username')
    
    if Account.objects.filter(email = email).exists():
        raise ValidationError("Email đã tồn tại")
    
    if Account.objects.filter(username = username).exists():
        raise ValidationError("Tên tài khoản đã tồn tại")
    
    if len(password) < 5:
        raise ValidationError("Mật khẩu phải trên 5 kí tự.")
    
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
    email = data.get('email')
    password = data.get('password')
    
    user = authenticate(username = email  , password = password)
    if user is not None :
        return Response({"messang":"đã đăng nhập "} , status = status.HTTP_200_OK)
    else:
        return Response({"messang":"Đăng nhập thất bại"},status=status.HTTP_401_UNAUTHORIZED)
    

    