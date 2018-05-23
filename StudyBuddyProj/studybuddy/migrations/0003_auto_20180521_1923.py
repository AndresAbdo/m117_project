# Generated by Django 2.0.5 on 2018-05-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0002_studygroup_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='studygroups',
        ),
        migrations.AddField(
            model_name='studygroup',
            name='members',
            field=models.ManyToManyField(help_text='Select the Students that are a part of this StudyGroup', to='studybuddy.Student'),
        ),
    ]