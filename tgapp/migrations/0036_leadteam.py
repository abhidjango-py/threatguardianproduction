# Generated by Django 3.2.12 on 2023-01-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0035_remove_course_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='static/')),
                ('name', models.CharField(max_length=50)),
                ('desg', models.CharField(max_length=50)),
                ('twitter', models.URLField(max_length=50, null=True)),
                ('linkedin', models.URLField(max_length=50)),
                ('gmail', models.URLField(max_length=50)),
            ],
        ),
    ]
