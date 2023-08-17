# Generated by Django 4.2.2 on 2023-08-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orderp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='max character limit 255', max_length=255, verbose_name='Title of the your order')),
                ('description', models.TextField(verbose_name='your user description')),
                ('fullname', models.CharField(help_text='max 20 character ', max_length=20, verbose_name='Your name(Author)')),
            ],
            options={
                'verbose_name': 'orderpost',
                'verbose_name_plural': 'All Movie Posts',
            },
        ),
    ]
