# Generated by Django 3.2.12 on 2022-12-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0003_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
