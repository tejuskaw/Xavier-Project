# Generated by Django 3.1.7 on 2021-04-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0014_remove_material_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='thumb',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
