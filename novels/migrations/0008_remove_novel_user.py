# Generated by Django 3.1.1 on 2020-09-18 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0007_novel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='user',
        ),
    ]
