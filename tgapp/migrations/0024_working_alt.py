# Generated by Django 3.2.12 on 2022-12-12 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0023_gallery_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='working',
            name='alt',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]