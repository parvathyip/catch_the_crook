# Generated by Django 4.2.2 on 2023-06-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0004_register_dgp_email_register_station_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_wanted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanted_images', models.FileField(upload_to='')),
            ],
        ),
    ]
