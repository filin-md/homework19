from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Создание тега
@register.simple_tag
def mediapath(value):
    if value:
        result = f'/media/{value}'
        return mark_safe(result)
    return "#"


# Создание фильтра
@register.filter
def mediapath(value):
    if value:
        result = f'/media/{value}'
        return mark_safe(result)
    return "#"