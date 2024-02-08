from django import template
from datetime import datetime

register = template.Library()

@register.filter
def lower(value):
    return value.lower()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)