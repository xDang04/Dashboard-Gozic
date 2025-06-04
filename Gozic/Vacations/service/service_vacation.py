from django.shortcuts import get_object_or_404
from ..models import Vacation
from ..serializers import * 
from rest_framework.response import responses
from rest_framework import status
def get_all_vacation(username = None):
    vacation = Vacation.objects.all()
    if username:
        vacation = vacation.filter(name__icontains = username)
    return vacation

def post_vacation(data):
    serializer = VacatioSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return responses({"messange":"Đã thêm thành công"} , status = status.HTTP_201_CREATED)
    return responses(serializer.errors , status = status.HTTP_400_BAD_REQUEST)