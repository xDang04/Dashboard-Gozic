from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Account.models import Account
from .models import Request
from django.http import JsonResponse
from datetime import datetime, date
from django.contrib import messages
# Create your views here.


@login_required
def profile_view(request):
    user = request.user  # kiểu dữ liệu là Account
    return render(request, 'profile/layout_profile.html', {
        'user': user
    })

def settings(request):
    return render(request, 'profile/settings.html')

@login_required
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'profile/profile_vacations.html', {'requests': requests})

@login_required
def add_request_view(request):
    if request.method == 'POST':
        request_type = request.POST.get('requestType')
        time_type = request.POST.get('timeType')
        start_date_str = request.POST.get('startDate')
        end_date_str = request.POST.get('endDate')
        reason = request.POST.get('reason', '').strip()
        start_time_str = request.POST.get('startTime', '')
        end_time_str = request.POST.get('endTime', '')

        # Kiểm tra dữ liệu bắt buộc
        if not start_date_str:
            messages.error(request, "Missing start date.")
            return redirect('profile:add_request')
        if not end_date_str:
            messages.error(request, "Missing end date.")
            return redirect('profile:add_request')

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect('profile:add_request')

        # Nếu chế độ giờ thì kiểm tra giờ bắt đầu & kết thúc
        start_time = None
        end_time = None
        if time_type == 'hours':
            if not start_time_str or not end_time_str:
                messages.error(request, "Missing time range for hourly request.")
                return redirect('profile:add_request')
            try:
                start_time = datetime.strptime(start_time_str, '%H:%M').time()
                end_time = datetime.strptime(end_time_str, '%H:%M').time()
            except ValueError:
                messages.error(request, "Invalid time format.")
                return redirect('profile:add_request')
            if start_time >= end_time:
                messages.error(request, "Start time must be before end time.")
                return redirect('profile:add_request')

        # Tạo request
        Request.objects.create(
            user=request.user,
            request_type=request_type,
            time_type=time_type,
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            reason=reason
        )
        return redirect('profile:myvacation')
    return render(request, 'profile/profile_vacations.html')