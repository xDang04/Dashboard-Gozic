from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse

# Create your views here.
@login_required
def add_support(request):
    if request.method == "POST":
        field = request.POST.get("fieldSupport")
        support = request.POST.get("support")
        getField = Field.objects.get(name=field)
        newSupport = Support.objects.create(content = support, author = request.user)
        newSupport.field.add(getField)
        return JsonResponse({"success":True})
    return JsonResponse({"success":False})
    