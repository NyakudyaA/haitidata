# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionbbox',
            name='srid',
            field=models.CharField(default=b'EPSG:4326', max_length=255),
        ),
    ]
