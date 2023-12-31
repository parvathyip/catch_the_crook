# Generated by Django 4.2.2 on 2023-06-26 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0007_alter_register_wanted_wanted_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_wanted',
            name='wanted_images',
        ),
        migrations.CreateModel(
            name='Wanted_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanted_images', models.ImageField(upload_to='')),
                ('wanted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_app.register_wanted')),
            ],
        ),
    ]
