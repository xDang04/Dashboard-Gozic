from .service.service_account import *
from .serializers import *
from django.shortcuts import render, redirect
from .service.service_account import  login_account
from .models import Account
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)  
            return redirect('projects_view')  
        else:
            return render(request, "account/login.html", {"error": "Email hoặc mật khẩu không đúng."})
    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "phone": request.POST.get("phone"),
            "birthday": request.POST.get("birthday"),
            "age": request.POST.get("age"),
            "position": request.POST.get("position"),
            "location": request.POST.get("location"),
            "company": request.POST.get("company"),
            "skype": request.POST.get("skype"),
        }

        try:
            account = create_account(data)
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return render(request, "account/register.html")