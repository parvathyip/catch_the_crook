# Generated by Django 4.2.2 on 2023-06-26 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_dgp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='')),
                ('job_status', models.CharField(max_length=20)),
                ('office_address', models.CharField(max_length=30)),
                ('office_district', models.CharField(max_length=15)),
                ('user_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
