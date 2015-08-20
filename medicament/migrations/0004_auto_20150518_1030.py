# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0003_auto_20150518_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc2',
            name='p3_10',
            field=models.CharField(null=True, max_length=80, verbose_name='КолПр3_10', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_6',
            field=models.CharField(null=True, max_length=80, verbose_name='КолПр3_6', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_7',
            field=models.CharField(null=True, max_length=80, verbose_name='КолПр3_7', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_8',
            field=models.CharField(null=True, max_length=80, verbose_name='КолПр3_8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_9',
            field=models.CharField(null=True, max_length=80, verbose_name='КолПр3_9', blank=True),
            preserve_default=True,
        ),
    ]
