# Generated by Django 2.2 on 2019-05-23 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0002_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='localization',
            new_name='location',
        ),
    ]