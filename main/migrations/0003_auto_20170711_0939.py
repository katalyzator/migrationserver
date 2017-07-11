# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-11 09:39
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170711_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_kz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='name_kz',
        ),
        migrations.AddField(
            model_name='news',
            name='content_kg',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=1, upload_to='images/news', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='name_kg',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
    ]