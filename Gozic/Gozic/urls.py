"""
URL configuration for Gozic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
    openapi.Info(
        title="Gozic API",
        default_version='v1',
        description="Tài liệu API cho hệ thống Dashboard Gozic",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('Projects.urls')),
    path('vacation/', include('Vacations.urls')),
    path('' , include('Account.urls')),

    path('api/accounts/', include('Account.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    path('dashboard/', include('DashBoard.urls')),

    path('calendar/', include('Calendar.urls')),
    path('profile/', include('Profile.urls')),
    
    path('messenger/', include('Messenger.urls')),
    path('accounts/', include('allauth.urls')),
    path('infoportal/', include('InfoPortal.urls')),
    path("ckeditor/", include("ckeditor_custom.ckeditor_urls")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)