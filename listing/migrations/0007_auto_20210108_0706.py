# Generated by Django 2.2.17 on 2021-01-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0006_auto_20210108_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_expired',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_type',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Regular'), (1, 'No Reserve'), (2, 'Returning'), (3, 'Royalty')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='make',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Volve'), (2, 'BMW')], null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='manufacture_year',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='model',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'CS6'), (2, 'CS7'), (3, 'CS8'), (4, 'CS9')], null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]