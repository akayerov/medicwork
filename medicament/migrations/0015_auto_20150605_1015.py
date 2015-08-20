# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0014_role_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='email',
            field=models.EmailField(max_length=60, blank=True, null=True, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='contact',
            field=models.CharField(max_length=50, blank=True, null=True, verbose_name='Ответственный'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='tel',
            field=models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон'),
            preserve_default=True,
        ),
    ]
