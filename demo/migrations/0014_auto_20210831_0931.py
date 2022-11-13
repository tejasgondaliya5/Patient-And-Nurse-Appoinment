# Generated by Django 3.2.3 on 2021-08-31 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0013_delete_usersearch'),
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
        migrations.AddField(
            model_name='nurseshedule',
            name='Aname',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.addnurse'),
        ),
    ]
