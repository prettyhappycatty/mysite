# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20150318_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='user',
            field=models.ForeignKey(to='cms.User', verbose_name='ユーザ', default=1, related_name='impressions'),
            preserve_default=True,
        ),
    ]
