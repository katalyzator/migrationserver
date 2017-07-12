# coding=utf-8
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .models import *
import json


def newsru_view(request):
    objects = Newsru.objects.all().reverse()
    objects_serialized = serializers.serialize('json', objects)
    return JsonResponse(json.dumps(objects_serialized, ensure_ascii=False, default=str).decode('utf8'), safe=False)


def newskg_view(request):
    objects = Newskg.objects.all()
    objects_serialized = serializers.serialize('json', objects)
    return JsonResponse(objects_serialized, safe=False)

