# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('naver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publisher',
            field=models.ForeignKey(to='naver.Publisher', related_name='authors', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(related_name='articles', to='naver.Author'),
        ),
    ]
