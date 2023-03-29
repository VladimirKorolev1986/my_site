from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

actor_movie = {'kianu_rivze': {'year_born': 1964,
                               'city_born': 'beirut',
                               'movie_name': 'On the crest of a wave'},
               'agnia': {'year_born': 2011,
                         'city_born': 'moscow',
                         'movie_name': 'Agnia searche her socks'}}
posts = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]


def main_page(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context=context)


# def posts(request):
#     return HttpResponse('Все посты блога')


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


def go_by_number(request, number_posts):
    context = {'number': number_posts}
    return render(request, 'blog/detail_by_number.html', context=context)


def go_by_string(request, string_posts):
    context = {'text': string_posts}
    return render(request, 'blog/detail_by_name.html', context=context)
