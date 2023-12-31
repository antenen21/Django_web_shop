# Generated by Django 4.1.7 on 2023-06-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_pump_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completeset',
            options={'ordering': ['my_order']},
        ),
        migrations.AlterModelOptions(
            name='fournisseur',
            options={'ordering': ['my_order'], 'verbose_name_plural': 'Fournisseur/shipper'},
        ),
        migrations.AlterModelOptions(
            name='puffer',
            options={'ordering': ['my_order']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['my_order']},
        ),
        migrations.AlterModelOptions(
            name='serviceaddons',
            options={'ordering': ['my_order']},
        ),
        migrations.AlterModelOptions(
            name='singlematerial',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='completeset',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='puffer',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pump',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serviceaddons',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='singlematerial',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
