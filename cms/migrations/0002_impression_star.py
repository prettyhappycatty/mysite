# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='star',
            field=models.IntegerField(verbose_name='評価', default=1),
            preserve_default=True,
        ),
    ]
