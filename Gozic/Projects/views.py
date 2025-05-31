from .models import *
from .serializers import *

from django.shortcuts import render

# Create your views here.

def projects_view(request):
    view_type = request.GET.get("view", "list")
    projects = Projects.objects.all()
    return render(request, "project/project.html", {
        "projects": projects,
        "view": view_type
    })
def project_add_view(request):
    return render(request, 'project/add_project.html')