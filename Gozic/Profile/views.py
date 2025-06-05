from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Account.models import Account
# Create your views here.

def myprofile(request):
    return render(request, 'profile/layout_profile.html')

@login_required
def profile_view(request):
    user = request.user  # kiểu dữ liệu là Account
    return render(request, 'layout_profile.html', {
        'user': user
    })