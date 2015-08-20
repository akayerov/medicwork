# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc2',
            name='p3_1',
            field=models.CharField(blank=True, verbose_name='КолПр3_1', max_length=80, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc2',
            name='p3_2',
            field=models.CharField(blank=True, verbose_name='КолПр3_2', max_length=80, null=True),
            preserve_default=True,
        ),
    ]
