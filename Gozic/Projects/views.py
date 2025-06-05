from django.shortcuts import render, redirect
from .models import Projects, Account
from .service.service_project import post_project  

def projects_view(request):
    view_type = request.GET.get("view", "list")
    projects = Projects.objects.all()
    accounts = Account.objects.all()
    return render(request, "project/project.html", {
        "projects": projects,
        "view": view_type,
        "accounts": accounts
    })

def project_add_view(request):
    accounts = Account.objects.all()

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "number": request.POST.get("number"),
            "description": request.POST.get("description"),
            "status": request.POST.get("status"),
            "create_at": request.POST.get("start_date"),   
            "dealine": request.POST.get("deadline"),
            "reporter": request.POST.get("reporter"),
            "assignees": request.POST.getlist("assignees"),  
        }

        response = post_project(data)

        if response.status_code == 201:
            return redirect("projects_view")
    return render(request, 'project/add_project.html', {'accounts': accounts})
