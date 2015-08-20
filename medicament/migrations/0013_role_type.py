# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0012_right_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='type',
            field=models.ForeignKey(to='medicament.Doc_type', default=1),
            preserve_default=False,
        ),
    ]
