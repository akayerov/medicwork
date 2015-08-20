# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0013_role_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='contact',
            field=models.CharField(verbose_name='Ответственный', default='Сидоров Иван Иванович', max_length=50),
            preserve_default=False,
        ),
    ]
