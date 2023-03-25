from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

actor_movie = {'kianu_rivze': {'year_born': 1964,
                               'city_born': 'beirut',
                               'movie_name': 'On the crest of a wave'},
               'agnia': {'year_born': 2011,
                         'city_born': 'moscow',
                         'movie_name': 'Agnia searche her socks'}}


def main_page(request):
    return render(request, 'blog/list_detail.html')


def posts(request):
    return HttpResponse('Все посты блога')


def movie(request, actor: str):
    description = actor_movie[actor]
    return render(request, f'blog/{actor}.html', context=description)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)
