from Calendar.models import Event
from Account.models import Account
from django.db.models.functions import ExtractMonth, ExtractDay

def get_accounts_for_month(year,month):
    accounts_in_month = Account.objects.annotate(
        b_month=ExtractMonth('birthday'),
        b_day=ExtractDay('birthday')
    ).filter(b_month=month)

    day_accounts_map = {}
    for acc in accounts_in_month:
        day = acc.birthday.day
        day_accounts_map.setdefault(day, []).append(acc)
    return day_accounts_map

def get_birthdays_in_month(month: int): 
    return Account.objects.filter(birthday__month=month)
