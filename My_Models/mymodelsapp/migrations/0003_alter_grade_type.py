# Generated by Django 3.2.3 on 2021-05-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodelsapp', '0002_auto_20210517_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='type',
            field=models.IntegerField(),
        ),
    ]
