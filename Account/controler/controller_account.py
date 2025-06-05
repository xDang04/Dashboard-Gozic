
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from ..service.service_account import *
from ..serializers import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class AccountViewSet(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_description="Lấy danh sách tài khoản",
        tags=['account']
    )
    def get(self,request):
        accounts = get_all_account()
        serializer = AccountSerializer(accounts, many = True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=AccountSerializer,
        operation_description="Tạo tài khoản mới" ,
        tags=['account']
    )
    def post(self , request):
        serializers = AccountSerializer(data = request.data)
        if serializers.is_valid():
           account = create_account( serializers.validated_data)
           return Response(AccountSerializer(account).data , status = status.HTTP_201_CREATED)
        return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)


class AccountDetailViewSet(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_description="Lấy danh sách tài khoản theo id",
        tags=['account']
    )
    def get(self,request,pk):
        accounts = get_all_account_by_id(pk = pk)
        serializer = AccountSerializer(accounts)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body= AccountSerializer ,
        operation_description="Cập nhật tài khoản ",
        tags=['account']
        )
    def put(self , request , pk):
        serializers = AccountSerializer(data = request.data)
        if serializers.is_valid():
            account = update_account(pk , serializers.validated_data)
            if account:
                return Response(AccountSerializer(account).data )
            return Response({'detail':'Not found'} , status= status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        operation_description="Xóa tài khoản theo id ",
        tags=['account']
        )
    def delete(self , request , pk):
        account = get_all_account_by_id(pk)
        delete_account(account )
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LoginSerializerView(APIView):
    permission_classes = [IsAuthenticated]         
    authentication_classes = [JWTAuthentication]
    permission_class = [AllowAny]
    @swagger_auto_schema(
        request_body=LoginSerializers,  # để hiện input khi đặt tên
        operation_summary="Đăng Nhập người dùng",
        operation_id="Đăng_nhập_người_dùng", 
        tags=["account"]
    )
    def post(self , request):
        return login_account(request.data)
        
            