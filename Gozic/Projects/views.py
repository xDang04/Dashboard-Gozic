from django.shortcuts import render, redirect
from .models import Projects, Account , Task
from .service.service_project import post_project  

def projects_view(request):
    view_type = request.GET.get("view", "list")
    projects = Projects.objects.all()
    accounts = Account.objects.all()

    return render(request, "project/project.html", {
        "projects": projects,
        "view": view_type,
        "accounts": accounts,
    })
def projects_detail(request):
    view_type = request.GET.get("view", "list")
    project_id = request.GET.get("project_id")
    projects = Projects.objects.all()
    accounts = Account.objects.all()
    tasks = Task.objects.none()
    backlog_tasks = Task.objects.none()
    selected_project = None
    if project_id:
        try:
            selected_project = Projects.objects.get(id = project_id)
            tasks = Task.objects.filter(project = selected_project).exclude(status="Backlog")
            backlog_tasks = Task.objects.filter(project = selected_project , status = "Backlog")
        except Projects.DoesNotExist:
            selected_project = None
    return render(request, "project/project_detail.html", {
        "projects": projects,
        "tasks": tasks,
        "backlog_tasks":backlog_tasks  ,
        "view": view_type,
        "accounts": accounts,
        "selected_project": selected_project,
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
