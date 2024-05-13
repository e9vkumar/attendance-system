from django import template


register = template.Library()

@register.simple_tag
def times(num):
    return range(num)