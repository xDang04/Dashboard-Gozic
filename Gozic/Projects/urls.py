# Projects/urls.py
from django.urls import path
from .views import *
from .controller.controller_project import *

urlpatterns = [
    path('api/project', ProjectViewSet.as_view(), name='project-list'),  
    path('api/project/<int:pk>/', ProjectDetailViewSet.as_view(), name='project-detail'),
    path('api/tasks/', TaskViewSet.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailViewSet.as_view(), name='task-detail'),

    path('ui/', projects_view, name='projects_view'),
    path('add/', project_add_view, name='add_project'),  
    path('projects_detail/', projects_detail, name='projects_detail'),  
    
]