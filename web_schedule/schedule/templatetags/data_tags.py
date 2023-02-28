from django import template
from schedule.models import *

register = template.Library()


@register.simple_tag(name="Days")
def get_days():
    return Days.objects.all()

