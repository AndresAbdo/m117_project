# Generated by Django 2.0.5 on 2018-05-31 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0007_auto_20180531_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studygroup',
            old_name='meeting_days_2',
            new_name='meeting_days',
        ),
    ]