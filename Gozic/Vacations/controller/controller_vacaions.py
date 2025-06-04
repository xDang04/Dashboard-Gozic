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

   