import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def style_file_links(value):
    breakpoint()
    pattern = r'<a.*?href="(/media/[\w/.-]+\.(docx|pdf|zip|rar|xlsx))".*?>.*?<\/a>'

    def replacer(match):
        file_url = match.group(1)
        filename = file_url.split('/')[-1]
        return f'<a href="{file_url}" class="file-preview">📎 {filename}</a>'

    styled_content = re.sub(pattern, replacer, value)
    return mark_safe(styled_content)
