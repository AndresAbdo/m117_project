# Generated by Django 2.0.5 on 2018-05-31 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0005_remove_studygroup_meeting_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studygroup',
            old_name='meeting_days_2',
            new_name='meeting_days',
        ),
    ]
