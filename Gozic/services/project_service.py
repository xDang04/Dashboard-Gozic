from Projects.models import Projects
from datetime import datetime, date
from Profile.models import TimeOffRequest

def get_all_projects():
    return Projects.objects.prefetch_related('assignees').select_related('reporter').all()

def calculate_hours(request_obj):
    """Tính số giờ xin nghỉ nếu là request theo giờ"""
    if request_obj.start_time and request_obj.end_time:
        delta = datetime.combine(date.min, request_obj.end_time) - datetime.combine(date.min, request_obj.start_time)
        return delta.total_seconds() / 3600
    return 0