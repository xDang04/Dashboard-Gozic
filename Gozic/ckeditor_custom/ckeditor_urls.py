# ckeditor_urls.py
from django.urls import path
from ckeditor_uploader import views as ckeditor_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('browse/', login_required(ckeditor_views.browse), name='ckeditor_browse'),
]
