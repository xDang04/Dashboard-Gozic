# Projects/urls.py
from django.urls import path
from .views import *
from .controller.controller_vacaions import *

urlpatterns = [
    path('api/vacation', VacationViewSet.as_view(), name='vacation-list'),  
     
    
]
 