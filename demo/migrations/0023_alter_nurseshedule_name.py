# Generated by Django 3.2.3 on 2021-08-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0022_rename_aname_nurseshedule_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurseshedule',
            name='Name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
