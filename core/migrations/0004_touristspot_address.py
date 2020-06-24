# Generated by Django 3.0.7 on 2020-06-24 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('core', '0003_touristspot_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
            preserve_default=False,
        ),
    ]
