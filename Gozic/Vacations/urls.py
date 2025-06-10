# Projects/urls.py
from django.urls import path
from .views import *
from .controller.controller_vacaions import *

urlpatterns = [
    path('api/vacation', VacationViewSet.as_view(), name='vacation-list'),  
    path('vacationdetail/<int:pk>', VacationDetailViewSet.as_view(), name='vacationdetail-list'),   
    path(" ", vacation_view, name="vacations_view"),
    path('add_vacation/', add_vacation, name='add_vacation'),  
    
]
 