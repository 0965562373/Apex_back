# Generated by Django 3.2.24 on 2024-03-05 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_api', '0006_auto_20240304_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='qualification',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mobile_no',
        ),
    ]
