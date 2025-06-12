from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.decorators.http import require_POST 
from .models import Projects, Account , Task
from .service.service_project import post_project  
from .service.service_task import post_task

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
        "status_choices": Task.STATUS_CHOICES
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

def add_task_view(request):
    projects = Projects.objects.all()
    accounts = Account.objects.all()
    if request.method == "POST":
        data = {
            "name" : request.POST.get("name"),
            "description" : request.POST.get("description"),
            "priority":request.POST.get("priority"),
            "status": request.POST.get("status"),
            "create_at": request.POST.get("start_date"), 
            "dealine": request.POST.get("deadline"),
            "assignees": request.POST.getlist("assignees"),  
            "project": request.POST.get("project")
        }
        response = post_task(data)
        if response.status_code == 201:
            return redirect("projects_detail")
    return render(request , "project/add_task.html",{'accounts': accounts ,'projects': projects})


def update_task_status_view(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('status')

        if task_id and new_status:
            try:
                task = Task.objects.get(id=task_id)
                task.status = new_status
                task.save()

                response = HttpResponse(status=200)
                response['HX-Redirect'] = request.META['HTTP_REFERER']
                return response

            except Task.DoesNotExist:
                return HttpResponse(status=404)
            except Exception as e:
                return HttpResponse(status=500, content=str(e))
        else:
            return HttpResponse(status=400, content="Missing task_id or status")
    else:
        return HttpResponse(status=405) 