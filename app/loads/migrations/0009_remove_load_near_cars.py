# Generated by Django 4.2.11 on 2024-03-25 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0008_alter_loadcarrelation_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='load',
            name='near_cars',
        ),
    ]
