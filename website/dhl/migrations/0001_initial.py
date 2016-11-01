# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderId', models.CharField(max_length=128)),
                ('senderId', models.IntegerField(max_length=64)),
                ('premiumUser', models.BooleanField(max_length=1)),
                ('packageImage', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to='dhl.BrokerUser')),
            ],
        ),
    ]
