# Generated by Django 3.2.9 on 2021-11-04 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='prority',
            new_name='priority',
        ),
    ]
