from django.urls import path
from .views import *
from .controler.controller_account import *

urlpatterns = [
    
    path('', AccountViewSet.as_view(), name='account-list'),
    path('account/', LoginSerializerView.as_view(), name='accout'),
    path('<int:pk>/', AccountDetailViewSet.as_view(), name='account-detail'),
    path('login/', login_view, name='login'),
    
]