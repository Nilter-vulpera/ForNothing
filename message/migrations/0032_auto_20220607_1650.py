# Generated by Django 3.1.13 on 2022-06-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0031_auto_20220607_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
