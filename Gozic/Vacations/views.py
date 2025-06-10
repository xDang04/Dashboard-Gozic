from django.shortcuts import render, redirect
from .models import Vacation
from Account.models import Account
from django.utils import timezone

def vacation_view(request):
    vacations = Vacation.objects.select_related('account').all()
    context = {
        'vacation_records': vacations
    }
    return render(request, 'vacation/vacation.html', context)

def add_vacation(request):
    accounts = Account.objects.all()
    error = None

    if request.method == "POST":
        try:
            account_id = request.POST.get("account")
            sick = int(request.POST.get("sick_leave", 0))
            remote = int(request.POST.get("work_remotely", 0))
            year = int(request.POST.get("year"))

            account = Account.objects.get(id=account_id)

            Vacation.objects.create(
                account=account,
                sick_leave=sick,
                work_remotely=remote,
                year=year,
                updated_at=timezone.now()
            )
            return redirect("vacations_view")
        except Exception as e:
            error = str(e)

    return render(request, "vacation/add_vacation.html", {"accounts": accounts, "error": error})