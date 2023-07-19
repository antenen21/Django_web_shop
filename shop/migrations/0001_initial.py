# Generated by Django 4.1.7 on 2023-06-10 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('postal_code', models.CharField(max_length=5, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Fournisseur/shipper',
            },
        ),
        migrations.CreateModel(
            name='Puffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=80)),
                ('capacity', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True, default=0.0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='products')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=50, null=True)),
                ('power', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True)),
                ('COP', models.FloatField(blank=True, default=0.0)),
                ('price', models.FloatField(blank=True, default=0.0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='products')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, null=True)),
                ('comment', models.TextField(max_length=200, null=True)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
