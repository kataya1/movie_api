# Generated by Django 3.2.9 on 2021-11-13 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pintrest', '0005_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
