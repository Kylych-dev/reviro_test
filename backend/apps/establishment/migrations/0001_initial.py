# Generated by Django 5.0.2 on 2024-02-26 06:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('locations', models.CharField(max_length=255, verbose_name='Locations')),
                ('opening_hours', models.CharField(max_length=100, verbose_name='Opening Hours')),
                ('requirements', models.TextField(verbose_name='Requirements')),
            ],
            options={
                'verbose_name': 'Establishment',
                'verbose_name_plural': 'Establishments',
            },
        ),
    ]
