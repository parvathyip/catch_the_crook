# Generated by Django 4.2.2 on 2023-06-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0013_add_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_complaint',
            name='crime_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='add_complaint',
            name='missing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
