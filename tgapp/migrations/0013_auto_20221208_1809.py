# Generated by Django 3.2.12 on 2022-12-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0012_linkservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.AlterField(
            model_name='linkservices',
            name='link',
            field=models.TextField(max_length=50),
        ),
    ]