# Generated by Django 4.2.2 on 2023-08-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_birthdate_optional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='First_Name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Confirm_Password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Current_Password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='New_Password',
        ),
    ]