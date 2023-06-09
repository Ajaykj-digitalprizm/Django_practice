# Generated by Django 4.2.1 on 2023-05-18 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_reader',
            name='Allocated_Quantity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='csv_reader',
            name='Available_Quantity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='csv_reader',
            name='Divider',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='csv_reader',
            name='Price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='csv_reader',
            name='Quantity_In_Stock',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
