# Generated by Django 4.1 on 2022-09-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place2',
            name='img',
            field=models.ImageField(height_field=100, upload_to='pics', width_field=100),
        ),
    ]
