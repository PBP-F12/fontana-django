# Generated by Django 4.2.6 on 2023-12-04 09:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_id',
            field=models.UUIDField(default=uuid.UUID('090119e8-0060-4629-9cc6-97e7e079ceab'), primary_key=True, serialize=False),
        ),
    ]
