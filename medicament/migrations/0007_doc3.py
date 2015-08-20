# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0006_auto_20150518_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc3',
            fields=[
                ('document_ptr', models.OneToOneField(serialize=False, to='medicament.Document', parent_link=True, auto_created=True, primary_key=True)),
                ('c1_1_1', models.IntegerField(verbose_name='Кол1_1_1', default=0)),
                ('c1_1_2', models.IntegerField(verbose_name='Кол1_1_2', default=0)),
                ('c1_2', models.IntegerField(verbose_name='Кол1_2', default=0)),
                ('c2_1', models.IntegerField(verbose_name='Кол2_1', default=0)),
                ('c2_2', models.IntegerField(verbose_name='Кол2_2', default=0)),
                ('c3_1', models.IntegerField(verbose_name='Кол3_1', default=0)),
                ('c3_2_1', models.IntegerField(verbose_name='Кол3_2_1', default=0)),
                ('c3_2_2', models.IntegerField(verbose_name='Кол3_2_2', default=0)),
                ('c4_1', models.IntegerField(verbose_name='Кол4_1', default=0)),
            ],
            options={
            },
            bases=('medicament.document',),
        ),
    ]
