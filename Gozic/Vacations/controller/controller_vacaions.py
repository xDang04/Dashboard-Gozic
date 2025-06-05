from ..serializers import * 
from ..service.service_vacation import * 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

class VacationViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    @swagger_auto_schema(
        operation_description="Lấy kì nghỉ của nhân viên",
        manual_parameters=[
            openapi.Parameter(
                'username',openapi.IN_QUERY , description="tìm kiếm kì nghỉ" , type = openapi.TYPE_STRING
            )
        ],
        tags=['Vacation'] 
    )
    def get(self , request):
        username = request.GET.get('username')
        vacation = get_all_vacation(username)
        serializer = VacatioSerializers(vacation , many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=VacatioSerializers,
        operation_summary="Thêm kì nghỉ",
        operation_id="Thêm kì nghỉ",
        tags=["Vacation"]
    )
    def post(self , request):
        return post_vacation(request.data , request.user)
    
class VacationDetailViewSet(APIView):
    permission_classes = [IsAuthenticated]         
    authentication_classes = [JWTAuthentication] 
    @swagger_auto_schema(
        operation_summary="Lấy chi tiết ngày nghỉ theo ID",
        tags=["Vacation"]
    )
    def get(self,request, pk):
        return get_vacation_by_id(pk)
    
    @swagger_auto_schema(
        request_body=VacatioSerializers,
        operation_summary="cập nhật kì nghỉ",
        operation_id="cập nhật kì nghỉ",
        tags=["Vacation"]
    )
    def put(self,request, pk):
        return put_vacation(pk , request.data , request.user) 
    
    @swagger_auto_schema(
        operation_summary="xóa kì nghỉ",
        operation_id="xóa kì nghỉ",
        tags=["Vacation"]
    )
    def delete(self , request , pk):
        return delete_vacation(pk )