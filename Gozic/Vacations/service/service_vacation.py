from django.shortcuts import get_object_or_404
from ..models import Vacation
from ..serializers import * 
from Account.models import *
from rest_framework.response import Response
from rest_framework import status
def get_all_vacation(username = None):
    vacation = Vacation.objects.all()
    if username:
        vacation = vacation.filter(name__icontains = username)
    return vacation

def post_vacation(data , user ):
    serializer = VacatioSerializers(data = data)
    if serializer.is_valid():
        serializer.save(account = user)
        return Response({"messange":"Đã thêm thành công"} , status = status.HTTP_201_CREATED)
    return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

def get_vacation_by_id(pk):
    vacation =  get_object_or_404(Vacation ,pk = pk)
    serializer = VacatioSerializers(vacation)
    return Response(serializer.data)

def put_vacation(pk, data, user):
    vacation = get_object_or_404(Vacation, pk=pk)
    
    serializer = VacatioSerializers(vacation, data=data)
    
    if serializer.is_valid():
        serializer.save(account=user)  
        return Response({"message": "Đã cập nhật kỳ nghỉ thành công"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_vacation(data , user ,pk):
    try :
        vacation = Vacation.objects.get(pk = pk) 
        vacation.delete
        return Response({"message":"Xóa dự án thành công"} , status= status.HTTP_201_CREATED)
    except:
        return Response({"message":"Xóa dự án thành công"} , status= status.HTTP_400_BAD_REQUEST)