# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class Newsru(models.Model):
    class Meta:
        verbose_name_plural = 'Новости на русском языке'
        verbose_name = 'Новость'

    name = models.CharField(max_length=255, verbose_name='Заголовок новости')

    content = RichTextUploadingField(verbose_name='Текст новости')

    image = models.ImageField(upload_to='images/news', verbose_name='Картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Newskg(models.Model):
    class Meta:
        verbose_name_plural = 'Новости на кыргызском языке'
        verbose_name = 'Новость'

    name = models.CharField(max_length=255, verbose_name='Заголовок новости')

    content = RichTextUploadingField(verbose_name='Текст новости')

    image = models.ImageField(upload_to='images/news', verbose_name='Картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)
