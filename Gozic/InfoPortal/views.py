from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from InfoPortal.models import Page, Folder
from .forms import FolderCreateForm,PageForm
from django.db.models import Count
from Account.models import Account
import random
# Create your views here.

color_options = [
    {"bg": "bg-blue-100", "text": "text-blue-600"},
    {"bg": "bg-yellow-100", "text": "text-yellow-600"},
    {"bg": "bg-green-100", "text": "text-green-600"},
    {"bg": "bg-purple-100", "text": "text-purple-600"},
    # ... thêm màu nếu muốn
]
@login_required
def infoPortal(request):
    allFolder = Folder.objects.annotate(page_count=Count('pages')).filter(user=request.user).prefetch_related('pages')
    for folder in allFolder:
        folder.color = random.choice(color_options)
    formFolder = FolderCreateForm()
    return render(request,'InfoPortal/info_portal.html',{"formFolder":formFolder, "allFolder":allFolder})

@login_required
def addInfoPortal(request):
    if request.method == "POST":
        form = FolderCreateForm(data=request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            
            folder.save()
            folder.user.add(request.user)
        return redirect('infoPortal')
            
    else:
        return redirect('infoPortal')
    
@login_required        
def insidefolder(request,id):
    folder= Folder.objects.prefetch_related('pages').get(id=id)
    formPage = PageForm()
    formFolder = FolderCreateForm()
    return render(request, "InfoPortal/insideFolder.html",{"POFolder":folder, "formPage":formPage,'formFolder':formFolder})


@login_required
def addPage(request,id):
    if request.method == 'POST':
        breakpoint()
        form = PageForm(request.POST)
        crrFolder = Folder.objects.get(id=id)
        if form.is_valid():
            page = form.save(commit=False)
            
            page.save()
            page.folder.add(crrFolder)
            return redirect('insidefolder', id) 
    else:
        form = PageForm()

    return render(request, 'addPage.html', {'form': form})


@login_required
def update_page(request,id):
    if request.method == "GET":
        page = get_object_or_404(Page, pk=id)
        folderId = page.folder.first().id
        form = PageForm(instance=page)
        return render(request, "InfoPortal/modal/updatePage.html",{'form':form,'folderID':folderId,'pageID':id})
    else:
        page = get_object_or_404(Page, pk=id)
        folderId = page.folder.first().id
        form = PageForm(data=request.POST, instance=page)
        if form.is_valid():
            form.save()
        return redirect('insidefolder', folderId)
   
@login_required
def shareFolder(request,folderId):
    if request.method == "POST":
        userEmail = request.POST.get('user_email')
        user = Account.objects.get(email__icontains=userEmail)
        folder = Folder.objects.get(id=folderId)
        folder.user.add(user)
    return redirect('insidefolder', folderId)