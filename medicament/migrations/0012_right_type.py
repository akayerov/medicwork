# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('medicament', '0011_auto_20150528_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Right_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('group', models.ForeignKey(to='auth.Group')),
                ('type', models.ForeignKey(to='medicament.Doc_type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
