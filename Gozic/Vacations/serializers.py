from rest_framework import serializers
from .models import *

class VacatioSerializers(serializers.ModelSerializer):
    username = serializers.CharField(source = 'account.username' , read_only = True)
    class Meta:
        model = Vacation
        fields = [ "id","username","sick_leave","work_remotely","year","created_at" ,"updated_at"]
        

        
 