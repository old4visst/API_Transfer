# Generated by Django 4.2.11 on 2024-03-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0007_loadcarrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadcarrelation',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=100, null=True),
        ),
    ]