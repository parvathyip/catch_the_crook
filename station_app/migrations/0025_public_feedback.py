# Generated by Django 4.2.2 on 2023-06-29 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0024_add_complaint_witness_district_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Public_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_app.register_public')),
                ('wanted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_app.register_wanted')),
            ],
        ),
    ]