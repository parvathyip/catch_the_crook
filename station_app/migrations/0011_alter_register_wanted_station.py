# Generated by Django 4.2.2 on 2023-06-26 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0010_rename_dgp_register_wanted_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_wanted',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='station_app.register_station'),
        ),
    ]
