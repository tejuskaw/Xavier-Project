# Generated by Django 3.0.4 on 2020-04-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question1',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question5',
        ),
    ]