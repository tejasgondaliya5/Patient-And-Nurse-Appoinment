# Generated by Django 3.2.3 on 2021-08-31 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0020_nurseshedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nurseshedule',
            old_name='Name',
            new_name='AName',
        ),
    ]