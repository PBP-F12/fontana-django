# Generated by Django 4.2.6 on 2023-12-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0006_alter_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/profile'),
        ),
    ]
