# Generated by Django 3.2.3 on 2021-09-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0047_cart_joinshedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Trigger',
            field=models.IntegerField(default=0),
        ),
    ]