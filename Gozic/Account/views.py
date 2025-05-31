from .service.service_account import *
from .serializers import *
from django.shortcuts import render, redirect
# Create your views here.
def login_view(request):
    accounts = Account.objects.all()
    if request.method == "POST":
        data =  {
            "email" : request.POST.get("email"),
            "password" : request.POST.get("password")
        }
        respone = login_account(data)
        if respone.status_code == 201:
            return redirect ("project.html")
    return render(request , "account/login.html")