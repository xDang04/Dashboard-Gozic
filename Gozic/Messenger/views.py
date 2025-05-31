from django.shortcuts import render

# Create your views here.
def messenger(request):
    return render(request, 'Messenger/messenger.html')