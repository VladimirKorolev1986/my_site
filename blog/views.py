from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def main_page(request):
    res = render_to_string('blog/index.html')
    return HttpResponse(res)


def posts(request):
    return HttpResponse('Все посты блога')

