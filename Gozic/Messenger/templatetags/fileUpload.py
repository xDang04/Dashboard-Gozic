import re
from django import template
from django.utils.safestring import mark_safe
from urllib.parse import unquote

register = template.Library()

@register.filter(name='fileUpload')
def fileUpload(value):
    # Bọc phần muốn bắt làm group(1)
    pattern = r'(/media/[\w/.\-%]+?\.(docx|pdf|zip|rar|xlsx))'

    def replacer(match):
        file_url = unquote(match.group(1))
        filename = file_url.split('/')[-1]
        return f'<a href="{file_url}" class="file-preview">📎 {filename}</a>'

    styled_content = re.sub(pattern, replacer, value)
    return mark_safe(styled_content)
