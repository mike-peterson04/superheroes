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


def edit_hero(request, hero_id ):
    if request.method == 'POST':
        hero = Hero.objects.get(pk=hero_id)
        hero.hero_name = request.POST.get('hero_name')
        hero.secret_identity = request.POST.get('secret')
        hero.primary = request.POST.get('primary')
        hero.secondary = request.POST.get('secondary')
        hero.catchphrase = request.POST.get('catchphrase')
        hero.save()
        return detail(request, hero_id)
    else:
        hero = Hero.objects.get(pk=hero_id)
        context = {
            'hero': hero
        }

        return render(request, 'heroes/edit.html', context)


def delete_hero(request, hero_id):
    Hero.objects.get(pk=hero_id).delete()

    return HttpResponseRedirect(reverse('heroes:index'))
