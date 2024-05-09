from django import template
from ..views import filter_record

register = template.library()

@register.filter
def func_caller(id,lower_date,upper_date):
    return filter_record(id=id,lower_range=lower_date,upper_range=upper_date)