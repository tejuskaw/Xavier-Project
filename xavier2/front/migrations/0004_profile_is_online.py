# Generated by Django 3.0.4 on 2021-04-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
