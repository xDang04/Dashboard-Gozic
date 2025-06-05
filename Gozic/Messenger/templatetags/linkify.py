# Messenger/templatetags/linkify.py
import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

URL_REGEX = r'(https?://[^\s]+)'

@register.filter(name='linkify')
def linkify(value):
    return mark_safe(re.sub(URL_REGEX, r'<a href="\1" target="_blank" style="color:blue; max-width:100%"><i class="fas fa-link"></i>\1</a>', value))
