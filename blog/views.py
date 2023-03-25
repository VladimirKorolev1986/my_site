from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

actor_movie = {'kianu_rivze': {'year_born': 1964,
                               'city_born': 'beirut',
                               'movie_name': 'On the crest of a wave'}}


def main_page(request):
    return render(request, 'blog/list_detail.html')


def posts(request):
    return HttpResponse('Все посты блога')


def movie(request, actor: str):
    description = actor_movie[actor]
    return render(request, 'blog/kianu_rivze.html', context=description)
