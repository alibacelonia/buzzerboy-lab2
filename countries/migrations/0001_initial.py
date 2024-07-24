# Generated by Django 5.0.7 on 2024-07-23 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('population', models.IntegerField()),
                ('description', models.TextField()),
                ('independence_day', models.DateField()),
                ('currency', models.CharField(max_length=50)),
                ('continent', models.CharField(choices=[('Africa', 'Africa'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('South America', 'South America'), ('Oceania', 'Oceania'), ('Antarctica', 'Antarctica')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('population', models.IntegerField()),
                ('description', models.TextField()),
                ('established_date', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='countries.country')),
            ],
        ),
    ]
