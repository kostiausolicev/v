# Generated by Django 3.1.4 on 2021-01-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veb', '0007_auto_20210125_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coors',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]