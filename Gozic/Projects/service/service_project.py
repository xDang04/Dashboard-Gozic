from Projects.models import Projects , Task
from Projects.serializers import * 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def get_all_project(name = None):
    project = Projects.objects.all()
    if name:
        project = project.filter(name__icontains=name)
    return project

def get_project_by_id(pk):
    return get_object_or_404(Projects , pk = pk)

def post_project(data):
    serializer = ProjectSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response({"messange":"Đã thêm thành công"} , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
def put_project(pk,data):
    try:
        project = Projects.objects.get(pk=pk)
    except Projects.DoesNotExist:
        return Response( status= status.HTTP_400_BAD_REQUEST)
    serializers = ProjectSerializers(project , data = data)
    if serializers.is_valid():
        serializers.save()
        return Response({"messange":"Đã cập nhật dự án thành công"} , status= status.HTTP_201_CREATED)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)
    
def delete_project(pk):
    try:
        project = Projects.objects.get(pk)
        project.delete()
        return Response({"messange":"Xóa dự án thành công"} , status= status.HTTP_201_CREATED)
    except:
        return Response({"messange":"Xóa dự án thành công"} , status= status.HTTP_400_BAD_REQUEST)
        
    