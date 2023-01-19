# Generated by Django 3.2.12 on 2022-12-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0009_auto_20221208_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='static/')),
                ('name', models.CharField(max_length=50)),
                ('desg', models.CharField(max_length=50)),
                ('linkedin', models.URLField(max_length=50)),
            ],
        ),
    ]