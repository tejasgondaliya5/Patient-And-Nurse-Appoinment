# Generated by Django 3.2.3 on 2021-08-31 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_auto_20210831_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurseshedule',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='nurseshedule',
            name='Specialist',
        ),
    ]
