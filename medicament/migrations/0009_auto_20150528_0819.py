# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0008_auto_20150522_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='action',
            field=models.CharField(verbose_name='Действие', choices=[('E', ''), ('O', 'На согласование'), ('Y', 'Согласовано'), ('N', 'Не согласовано'), ('C', 'Изменение')], default='E', max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc3',
            name='c4_1',
            field=models.FloatField(verbose_name='Кол4_1', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(verbose_name='Роль', choices=[('Р', 'Редактирование'), ('К', 'Контроль'), ('F', 'Администратор')], default='Р', max_length=1),
            preserve_default=True,
        ),
    ]
