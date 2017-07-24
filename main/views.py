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

    r = requests.post('http://www.ssm.gov.kg/blacklist/',
                      data={'fio': 'Кенешов', 'd': '19', 'm': '10', 'y': '1984'})

    id = r.text[5796:5801]

    name = r.text[5832:5860]

    link = 'http://www.ssm.gov.kg/blacklist/info/' + id
    # f = requests.get(link)
    # nakaz = (f.text).encode("utf-8")

    html = requests.get(link)
    text = html.text
    parsed_html = BeautifulSoup(text)

    nakaz = parsed_html.body.find('p').text

    l = Nakaz(name=nakaz, fio=name)
    l.save()

    item = Nakaz.objects.get(id=l.id)

    result = {'id': item.id, 'name': item.name, 'fio': item.fio}

    # dict_obj = model_to_dict(result)

    # data = serializers.serialize('json', [result, ])

    return JsonResponse(result)
