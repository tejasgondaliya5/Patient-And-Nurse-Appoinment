# Generated by Django 3.2.3 on 2021-09-01 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0034_remove_cart_joinnurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='joinNurse',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.addnurse'),
        ),
    ]