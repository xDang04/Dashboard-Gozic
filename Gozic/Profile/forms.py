from django import forms
from .models import TimeOffRequest

class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = [
            'leave_type', 'request_mode', 'start_date', 'end_date',
            'date', 'start_time', 'end_time', 'comment'
        ]
