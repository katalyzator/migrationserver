# coding=utf-8
from django.http import JsonResponse, HttpResponse
from .models import *
import requests
import json
from django.core import serializers
from django.forms.models import model_to_dict
import urllib


def newsru_view(request):
    objects = Newsru.objects.all().reverse()
    objects_serialized = serializers.serialize('json', objects)
    return JsonResponse(objects_serialized, safe=False)


def newskg_view(request):
    objects = Newskg.objects.all()
    objects_serialized = serializers.serialize('json', objects)
    return JsonResponse(objects_serialized, safe=False)


def blacklist_view(request):
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        from bs4 import BeautifulSoup

    fio = request.GET.get('fio')
    d = request.GET.get('d')
    m = request.GET.get('m')
    y = request.GET.get('y')

    r = requests.post('http://www.ssm.gov.kg/blacklist/',
                      data={'fio': fio, 'd': d, 'm': m, 'y': y})

    bs_r = BeautifulSoup(r.text)

    # id = r.text[5700:5801]
    if bs_r.find('a', {'class': 'bigs'}):
        id_link = bs_r.find('a', {'class': 'bigs'})['href']

    else:
        id_link = None

    print id_link

    if bs_r.body.find('a', {'class': 'bigs'}):
        name = bs_r.body.find('a', {'class': 'bigs'}).text
    else:
        name = None

    if id_link:

        link = 'http://www.ssm.gov.kg' + id_link

        html = requests.get(link)
        text = html.text
        parsed_html = BeautifulSoup(text)

        nakaz = parsed_html.body.find('p').text

    else:
        nakaz = None

    result = {'nakaz': nakaz, 'fio': name}

    return JsonResponse(dict(data=result))
