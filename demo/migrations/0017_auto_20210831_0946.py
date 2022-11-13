# Generated by Django 3.2.3 on 2021-08-31 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0016_auto_20210831_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurseshedule',
            name='Name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='nurseshedule',
            name='Specialist',
            field=models.CharField(choices=[('select', 'select'), ('Dentist', 'Dentist'), ('Homeyopethic', 'Homeyopethic'), ('Orthopedic', 'Orthopedic')], default='', max_length=20),
        ),
    ]
