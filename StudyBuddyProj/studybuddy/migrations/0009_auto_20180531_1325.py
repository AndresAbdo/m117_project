# Generated by Django 2.0.5 on 2018-05-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0008_auto_20180531_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='meeting_days',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=9),
        ),
    ]