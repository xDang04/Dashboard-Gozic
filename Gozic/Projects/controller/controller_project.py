from drf_yasg import openapi
from ..service.service_project import *
from ..service.service_task import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication


 
class ProjectViewSet(APIView):
    permission_classes = [IsAuthenticated]         
    authentication_classes = [JWTAuthentication]
    @swagger_auto_schema(
        operation_description="Lấy danh sách dự án",
        manual_parameters=[
            openapi.Parameter(
                'name',openapi.IN_QUERY , description="tìm kiếm sản phẩm" , type = openapi.TYPE_STRING
            )
        ],
        tags=['Project']
    )
    def get(self , request):
        name = request.GET.get('name')
        project = get_all_project(name)
        serializer = ProjectSerializers(project , many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ProjectSerializers,
        operation_summary="Thêm dự án",
        operation_id="Thêm dự án",
        tags=["Project"]
    )
    def post(self , request):
        return post_project(request.data)
    
class ProjectDetailViewSet(APIView):
    permission_classes = [IsAuthenticated]         
    authentication_classes = [JWTAuthentication] 
    @swagger_auto_schema(
        operation_summary="Lấy chi tiết danh mục theo ID",
        tags=["Project"]
    )
    def get(self,request, pk):
        return get_project_by_id(pk)
    @swagger_auto_schema(
        request_body=ProjectSerializers,
        operation_summary="cập nhật dự án",
        operation_id="cập nhật dự án",
        tags=["Project"]
    )
    def put(self , request , pk):
        return put_project(pk ,request.data)
    @swagger_auto_schema(
        operation_summary="Xoa dự án",
        operation_id="Xóa dự án",
        tags=["Project"]
    )
    def delete(self , request , pk):
        return delete_project(pk)
    
    
    
class TaskViewSet(APIView):
    permission_classes = [IsAuthenticated]         
    authentication_classes = [JWTAuthentication] 
    @swagger_auto_schema(
        operation_description="Lấy nhiệm vụ dự án",
        manual_parameters=[
            openapi.Parameter(
                'name',openapi.IN_QUERY , description="tìm kiếm sản phẩm" , type = openapi.TYPE_STRING
            )
        ],
        tags=['Task']
    )
    def get(self , request):
        name = request.GET.get('name')
        task = get_all_task(name)
        serializer = TaskSerializers(task , many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=TaskSerializers,
        operation_summary="Thêm nhiệm vụ của dự án",
        operation_id="Thêm nhiệm vụ của dự án",
        tags=["Task"]
    )
    def post(self , request):
        return post_task(request.data)
    
class TaskDetailViewSet(APIView):
    permission_classes = [IsAuthenticated]         
    authentication_classes = [JWTAuthentication] 
    @swagger_auto_schema(
        operation_summary="Lấy chi tiết nhiệm vụ của dự án theo ID",
        tags=["Task"]
    )
    def get(self,request, pk):
        return get_task_by_id(pk)
    @swagger_auto_schema(
        request_body=TaskSerializers,
        operation_summary="cập nhật nhiệm vụ của dự án",
        operation_id="cập nhật nhiệm vụ của dự án",
        tags=["Task"]
    )
    def put(self , request , pk):
        return put_task(pk ,request.data)
    @swagger_auto_schema(
        operation_summary="Xoa dự án",
        operation_id="Xóa dự án",
        tags=["Task"]
    )
    def delete(self , request , pk):
        return delete_task(pk)
    
    