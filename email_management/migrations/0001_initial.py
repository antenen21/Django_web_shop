# Generated by Django 4.2.3 on 2023-07-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_address', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('date', models.TimeField()),
            ],
        ),
    ]
