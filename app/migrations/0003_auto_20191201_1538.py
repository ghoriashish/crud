# Generated by Django 2.0 on 2019-12-01 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191201_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Fname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Lname',
            new_name='lname',
        ),
    ]
