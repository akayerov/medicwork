# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0002_auto_20150518_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc2',
            name='p3_3',
            field=models.CharField(verbose_name='КолПр3_3', null=True, max_length=80, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_4',
            field=models.CharField(verbose_name='КолПр3_4', null=True, max_length=80, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_5',
            field=models.CharField(verbose_name='КолПр3_5', null=True, max_length=80, blank=True),
            preserve_default=True,
        ),
    ]
