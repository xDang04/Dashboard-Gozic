from django.shortcuts import render, redirect
from datetime import date
from services import calendar_services
from services.calendar_services import get_accounts_for_month
from datetime import date, timedelta
import calendar
from Account.models import Account
from .models import Event
from django.views.decorators.csrf import csrf_protect

 
def calendar_view(request):
    year = int(request.GET.get('year', date.today().year))
    month = int(request.GET.get('month', date.today().month))

    first_day_of_month = date(year, month, 1)
    first_weekday = first_day_of_month.weekday()

    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    prev_month_last_day = calendar.monthrange(prev_year, prev_month)[1]

    # Ngày cuối cùng của tháng trước để chèn vào các ô trống đầu tuần
    empty_days = [
        prev_month_last_day - i for i in reversed(range(first_weekday))
    ]

    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    events = Event.objects.filter(date__year=year, date__month=month)
    event_map = {}
    for event in events:
        day = event.date.day
        event_map.setdefault(day, []).append(event)
    # Lấy dict ngày -> list account birthday ngày đó
    birthday_map = get_accounts_for_month(year, month)

    calendar_data = []  
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        current_date = date(year, month, day)
        if current_date.weekday() < 5:
            accounts = birthday_map.get(day, [])
            calendar_data.append({
                'day': day,
                'accounts': accounts,
                'events': event_map.get(day, [])
            })

    context = {
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': (month + 1) if month < 12 else 1,
        'next_year': year if month < 12 else year + 1,
        'weekdays': weekdays,
        'empty_days': empty_days,
        'calendar_data': calendar_data,
    }
    return render(request, 'calendar/calendar.html', context)


@csrf_protect
def add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        repeat = request.POST.get('repeat') == 'on'

        print(name, category, date)

        Event.objects.create(
            name=name,
            category=category,
            priority=priority,
            date=date,
            time=time,
            description=description,
            repeat=repeat
        )
        return redirect('calendar:calendar')  # hoặc URL bạn muốn quay về
    return redirect('calendar:calendar')