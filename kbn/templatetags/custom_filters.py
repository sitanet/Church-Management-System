# myapp/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter(name='youtube_id')
def youtube_id(value):
    """
    Extracts YouTube video ID from URL.
    """
    pattern = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+')
    match = pattern.match(value)
    if match:
        if 'youtu.be' in value:
            return value.split('/')[-1]
        elif 'youtube.com' in value:
            return value.split('v=')[-1].split('&')[0]
    return None
