# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0007_doc3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc2',
            name='c2_5_10',
            field=models.FloatField(default=0, verbose_name='Кол2_5_10'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_5_11',
            field=models.FloatField(default=0, verbose_name='Кол2_5_11'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc2',
            name='c2_5_12',
            field=models.FloatField(default=0, verbose_name='Кол2_5_12'),
            preserve_default=True,
        ),
    ]
