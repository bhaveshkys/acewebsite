# Generated by Django 2.2.4 on 2019-08-13 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_submission_folder'),
        ('portal', '0001_initial'),
        ('review', '0002_auto_20190812_2349'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'submission')},
        ),
    ]
