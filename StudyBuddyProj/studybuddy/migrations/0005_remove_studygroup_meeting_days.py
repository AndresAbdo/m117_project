# Generated by Django 2.0.5 on 2018-05-31 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0004_studygroup_meeting_days_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='meeting_days',
        ),
    ]
