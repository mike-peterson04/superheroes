from django.shortcuts import render
from .models import Hero


def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    hero = Hero.objects.filter(id=hero_id)
    context = {
        'hero': hero
    }

    return render(request, 'heroes/detail.html', context)
