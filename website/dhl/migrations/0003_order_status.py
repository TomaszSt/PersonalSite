# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhl', '0002_auto_20161030_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Not relevant'), (2, b'Review'), (3, b'Maybe relevant'), (4, b'Relevant'), (5, b'Leading candidate')]),
        ),
    ]
