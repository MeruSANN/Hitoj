# Generated by Django 2.2.24 on 2021-06-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0119_hide_problem_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_totp_timecode',
            field=models.IntegerField(default=0, verbose_name='last TOTP timecode'),
        ),
    ]
