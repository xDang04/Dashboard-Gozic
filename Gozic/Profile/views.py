from django.shortcuts import render, redirect
from services.project_service import get_all_projects, calculate_hours
from .forms import TimeOffRequestForm



def list_projects_view(request):
    projects = get_all_projects()
    return render(request, 'profile/profile_projects.html', {'projects': projects})

def vacation(request):
    return render(request, 'profile/profile_vacations.html')

def request_time_off_view(request):
    if request.method == 'POST':
        form = TimeOffRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            hours = calculate_hours(leave)
            leave.save()
            return redirect('success')
    else:
        form = TimeOffRequestForm()
    return render(request, 'profile/add_request.html', {'form': form})