# Generated by Django 4.2.6 on 2023-10-24 18:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0003_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('book_title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('avg_rating', models.FloatField()),
                ('num_rating', models.IntegerField()),
                ('image_link', models.CharField(blank=True, max_length=1024, null=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='upload/book/')),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.author')),
            ],
        ),
    ]
