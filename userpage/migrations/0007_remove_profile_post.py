# Generated by Django 3.0 on 2020-03-08 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0006_auto_20200308_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
