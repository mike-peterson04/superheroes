from django.shortcuts import render
from .models import Hero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    hero = Hero.objects.get(pk=hero_id)
    context = {
        'hero': hero
    }

    return render(request, 'heroes/detail.html', context)

def create_hero(request):
    if request.method == 'POST':
        hero_name = request.POST.get('hero_name')
        secret_identity = request.POST.get('secret')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Hero(hero_name=hero_name, secret_identity=secret_identity, primary=primary, secondary=secondary, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')
