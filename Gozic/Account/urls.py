from django.urls import path
from .views import *
from .controler.controller_account import *

urlpatterns = [ 
    path('account/api', AccountViewSet.as_view(), name='account-list'),
    path('account/', LoginSerializerView.as_view(), name='accout'),
    path('<int:pk>/', AccountDetailViewSet.as_view(), name='account-detail'),
    path('', login_view, name='login'), 
    path('register/', register_view, name='register'), 
]