# Generated by Django 4.2.3 on 2023-08-01 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_category_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='img',
        ),
    ]
