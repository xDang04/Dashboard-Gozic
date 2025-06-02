# Projects/urls.py
from django.urls import path
from .views import *
from .controller.controller_project import *

urlpatterns = [
    path('', ProjectViewSet.as_view(), name='project-list'),  
    path('<int:pk>/', ProjectDetailViewSet.as_view(), name='project-detail'),
    path('tasks/', TaskViewSet.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailViewSet.as_view(), name='task-detail'),

  
    path('ui/', projects_view, name='projects_view'),# http://127.0.0.1:8000/api/projects/ui/
    path('add/', project_add_view, name='add_project'),  # http://127.0.0.1:8000/api/projects/add/
]
