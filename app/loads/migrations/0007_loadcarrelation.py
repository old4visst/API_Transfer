# Generated by Django 4.2.11 on 2024-03-25 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('loads', '0006_load_near_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadCarRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=3, max_digits=100)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loads.load')),
            ],
        ),
    ]
