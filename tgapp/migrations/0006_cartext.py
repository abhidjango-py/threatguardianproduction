# Generated by Django 3.2.12 on 2022-12-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0005_auto_20221202_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
