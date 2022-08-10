from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *





def index(request):
    posts = Women.objects.all()
    # cats = Category.objects.all()
    context = {'title': 'Главная страница',  'posts': posts, 'cat_selected': 0}
    return render(request, 'women/index.html', context)


def show_post(request, post_id):
    post = Women.objects.get(pk=post_id)
    return render(request, 'women/single.html', {'post': post})


def get_categories(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404
    context = {'posts': posts, 'cat_selected': cat_id}
    return render(request, 'women/index.html', context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def add_page(request):
    return HttpResponse('Страница добавления статьи')


def contact(request):
    return HttpResponse('Страница контакта')


def login(request):
    return HttpResponse('Страница для входа сайта')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!!!</h1>')