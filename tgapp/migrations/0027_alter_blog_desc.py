# Generated by Django 3.2.12 on 2022-12-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0026_alter_blog_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.TextField(),
        ),
    ]