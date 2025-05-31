from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
# def messenger(request):
#     return render(request, 'Messenger/messenger.html')

def login(request):
    return render(request, 'login.html')


@login_required
def messenger(request):
    chat_group = get_object_or_404(ChatGroup, name="chat_group")
    chat_messages = chat_group.chat_messages.all()
    form = ChatmessageCreateForm()
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            
            message.save()
            context = {"message": message, "user": request.user}
            return render(request, 'Messenger/partials/chat_message_p.html', context)

        
    return render(request, 'Messenger/messenger.html',{"chat_messages":chat_messages, "form":form
                                                  })