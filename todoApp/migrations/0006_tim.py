# Generated by Django 3.2.4 on 2021-12-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0005_alter_task_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
            ],
        ),
    ]
