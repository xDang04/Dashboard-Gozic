from django.urls import path
from .views import *

urlpatterns = [
    path('', AccountViewSet.as_view(), name='account-list'),
    path('<int:pk>/', AccountDetailViewSet.as_view(), name='account-detail'),
    
]