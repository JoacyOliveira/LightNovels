# Generated by Django 3.1.1 on 2020-09-18 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0010_auto_20200918_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='user',
        ),
    ]
