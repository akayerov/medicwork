# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0009_auto_20150528_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc3',
            name='p4_2',
            field=models.CharField(verbose_name='КолПр3_38', max_length=80, blank=True, null=True),
            preserve_default=True,
        ),
    ]
