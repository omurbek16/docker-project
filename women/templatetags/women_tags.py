from django import template
from women.models import *


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add-page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
     ]

register = template.Library()


@register.simple_tag(name='get_categories')
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_menu():
    return menu