# Generated by Django 2.0.5 on 2018-05-22 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
