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
            name='c2_14_13',
            field=models.IntegerField(verbose_name='Кол2_14_13', default=0),
            preserve_default=True,
        ),
    ]
