# Generated by Django 4.2.2 on 2023-08-26 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Birthdate_Optional',
        ),
    ]
