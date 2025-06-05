from django.shortcuts import render
from .models import Vacation
from Account.models import Account

def vacation_view(request):
   
    vacations = Vacation.objects.select_related('account').all()

    context = {
        'vacation_records': vacations
    }
    return render(request, 'vacation/vacation.html', context)