# Generated by Django 4.2.2 on 2023-06-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0023_add_complaint_criminal_add_complaint_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_complaint',
            name='witness_district',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='add_complaint',
            name='witness_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='add_complaint',
            name='witness_fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='add_complaint',
            name='witness_lname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='add_complaint',
            name='witness_phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
