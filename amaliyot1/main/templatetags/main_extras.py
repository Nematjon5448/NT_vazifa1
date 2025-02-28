from django import template
from ..models import Brand, Rang


register = template.Library()

@register.simple_tag
def send_all_brand():
    return Brand.objects.all()

@register.simple_tag
def send_all_color():
    return Rang.objects.all()