from rest_framework import serializers
from .models import *

class ProjectSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields ='__all__'
        

class TaskSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields ='__all__'
        
