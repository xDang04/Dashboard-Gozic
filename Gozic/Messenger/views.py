from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from Account.models import Account
from django.http import Http404
import shortuuid
from django.db.models import OuterRef, Subquery

# Create your views here.
# def messenger(request):
#     return render(request, 'Messenger/messenger.html')

def login(request):
    return render(request, 'login.html')


@login_required
def messenger(request, chatroom_name = "chat_group"):
    allGroup = ChatGroup.objects.all()
    latest_messages = GroupMessage.objects.filter(
        group=OuterRef('pk')
    ).order_by('-created')
    allGroup = allGroup.annotate(
        lastest_message = Subquery(latest_messages.values("body")[:1]),
        lastest_time = Subquery(latest_messages.values("created")[:1]),
        lastest_sender = Subquery(latest_messages.values("author__username")[:1])
    )
    chat_group = get_object_or_404(ChatGroup, name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()
    form = ChatmessageCreateForm()
    other_user = None
    if not chat_group.is_group:
        if request.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            
            message.save()
            context = {"message": message, "user": request.user}
            return render(request, 'Messenger/partials/chat_message_p.html', context)

    context = {"chat_messages":chat_messages,
            "form":form,
            "other_user":other_user,
            "chatroom_name":chatroom_name,
            "allGroup":allGroup,
            "crrUser":request.user.username,
            "groupId":chat_group.id,
            "crrGroup":chat_group
    }
    return render(request, 'Messenger/messenger.html',context)
    

def get_or_create_chatroom(request, username):
    username = username.strip()
    # if request.user.username == username:
    #     return redirect('home')
   
    other_user = Account.objects.get(username=username)
    my_chatrooms = request.user.members_groups.filter(is_group = False)
    if my_chatrooms:
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all():
                chatroom = chatroom
                break
            else:
                chatroom = ChatGroup.objects.create(name=shortuuid.uuid(),is_group = False)
                chatroom.members.add(other_user,request.user)
    else:
        chatroom = ChatGroup.objects.create(name=shortuuid.uuid(),is_group = False)
        chatroom.members.add(other_user, request.user)
    
    return redirect('chatroom',chatroom.name)


def search(request, groupId):
    keySearch = request.GET.get('search', '')
    crrGroup = ChatGroup.objects.get(id=groupId)
    chat_search = crrGroup.chat_messages.filter(body__icontains=keySearch).order_by('-created')

    # Lấy lại các biến context cần thiết
    allGroup = ChatGroup.objects.all()
    latest_messages = GroupMessage.objects.filter(
        group=OuterRef('pk')
    ).order_by('-created')
    allGroup = allGroup.annotate(
        lastest_message=Subquery(latest_messages.values("body")[:1]),
        lastest_time=Subquery(latest_messages.values("created")[:1]),
        lastest_sender=Subquery(latest_messages.values("author__username")[:1])
    )
    form = ChatmessageCreateForm()
    other_user = None
    if not crrGroup.is_group:
        if request.user not in crrGroup.members.all():
            raise Http404()
        for member in crrGroup.members.all():
            if member != request.user:
                other_user = member
                break

    context = {
        "chat_messages": chat_search,
        "form": form,
        "other_user": other_user,
        "chatroom_name": crrGroup.name,
        "allGroup": allGroup,
        "crrUser": request.user.username,
        "groupId": crrGroup.id
    }
    return render(request, 'Messenger/messenger.html', context)