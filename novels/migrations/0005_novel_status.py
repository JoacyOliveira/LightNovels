# Generated by Django 3.1.1 on 2020-09-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0004_auto_20200915_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='status',
            field=models.CharField(choices=[(1, 'Andamento'), (2, 'Concluido')], default=1, max_length=50),
        ),
    ]