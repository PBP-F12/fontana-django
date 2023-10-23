# Generated by Django 4.2.6 on 2023-10-23 20:10

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auths.user',),
            managers=[
                ('author', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
