from Projects.serializers import TaskSerializers
from Projects.models import Projects , Task
from Projects.serializers import * 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def get_all_task(name = None):
    task = Task.objects.all()
    if name:
        task = Task.filter(name__icontains=name)
    return task

def get_task_by_id(pk):
    return get_object_or_404(Task , pk = pk)

def post_task(data):
    serializer = TaskSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response({"messange":"Đã thêm thành công"} , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
def put_task(pk,data):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response( status= status.HTTP_400_BAD_REQUEST)
    serializers = ProjectSerializers(task , data = data)
    if serializers.is_valid():
        serializers.save()
        return Response({"messange":"Đã cập nhật dự án thành công"} , status= status.HTTP_201_CREATED)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)
    
def delete_task(pk):
    try:
        task = Task.objects.all()
        task.delete()
        return Response({"messange":"Xóa dự án thành công"} , status= status.HTTP_201_CREATED)
    except:
        return Response({"messange":"Xóa dự án thành công"} , status= status.HTTP_400_BAD_REQUEST)
        
    