# Generated by Django 5.0.2 on 2024-02-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_merge_20240212_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='body_part',
        ),
        migrations.RemoveField(
            model_name='user',
            name='height',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='user',
            name='weight',
        ),
        migrations.AddField(
            model_name='user',
            name='isStaff',
            field=models.BooleanField(default=False),
        ),
    ]