# Generated by Django 3.0.7 on 2020-06-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200624_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='touristspots'),
        ),
    ]
