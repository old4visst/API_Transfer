# Generated by Django 4.2.11 on 2024-03-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('loads', '0005_remove_load_near_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='near_cars',
            field=models.ManyToManyField(default=None, related_name='near_cars', to='cars.car'),
        ),
    ]