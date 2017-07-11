from django.core import serializers
from django.http import JsonResponse
from .models import *


def newsru_view(request):
    objects = Newsru.objects.all().reverse()
    objects_serialized = serializers.serialize('json', objects)

    return JsonResponse(objects_serialized, safe=False)


def newskg_view(request):
    objects = Newskg.objects.all().reverse()
    objects_serialized = serializers.serialize('json', objects)

    return JsonResponse(objects_serialized, safe=False)
