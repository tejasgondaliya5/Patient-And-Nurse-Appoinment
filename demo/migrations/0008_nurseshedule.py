# Generated by Django 3.2.3 on 2021-08-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_booknurse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurseshedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Specialist', models.CharField(choices=[('select', 'select'), ('Dentist', 'Dentist'), ('Homeyopethic', 'Homeyopethic'), ('Orthopedic', 'Orthopedic')], default='', max_length=20)),
                ('Date', models.DateField()),
                ('Root', models.CharField(choices=[('select', 'select'), ('Morning', 'Morning'), ('Afternoot', 'Afternoot'), ('Evning', 'Evning')], default='', max_length=20)),
                ('Start_time', models.TimeField(auto_now_add='False')),
                ('End_time', models.TimeField(auto_now_add='False')),
            ],
        ),
    ]
