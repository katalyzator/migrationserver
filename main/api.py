from tastypie.contrib.gis.resources import ModelResource

from .models import *

api_object_newsru = Newsru.objects.all()
api_object_newskg = Newskg.objects.all()


class NewsruResource(ModelResource):
    class Meta:
        queryset = api_object_newsru
        name = 'Newsru'
        limit = 1000


class NewskgResource(ModelResource):
    class Meta:
        queryset = api_object_newsru
        name = 'Newskg'
        limit = 1000
