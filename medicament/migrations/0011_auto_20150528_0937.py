# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0010_doc3_p4_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc3',
            old_name='p4_2',
            new_name='c4_2',
        ),
    ]
