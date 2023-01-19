# Generated by Django 3.2.12 on 2023-01-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0027_alter_blog_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/')),
                ('heading', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('start', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='static/')),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
