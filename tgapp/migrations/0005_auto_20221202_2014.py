# Generated by Django 3.2.12 on 2022-12-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0004_apply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='option',
        ),
        migrations.AddField(
            model_name='apply',
            name='opt',
            field=models.CharField(default='Just Connecting', max_length=20),
        ),
    ]
