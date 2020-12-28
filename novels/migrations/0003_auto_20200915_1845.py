# Generated by Django 3.1.1 on 2020-09-15 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0002_auto_20200915_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='chapter',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='novel',
            name='image',
            field=models.ImageField(null=True, upload_to='novels_images'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='link',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
