# Generated by Django 5.0.1 on 2024-01-23 07:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_id', models.IntegerField(unique=True)),
                ('street', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('previous_job_count', models.IntegerField()),
                ('amount_due', models.IntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]