# Generated by Django 4.2.2 on 2023-08-19 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_color_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppagemodel',
            name='Availability',
            field=models.CharField(default=django.utils.timezone.now, help_text='max character limit 255', max_length=255, verbose_name='Availability'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppagemodel',
            name='Brands',
            field=models.CharField(default=django.utils.timezone.now, help_text='max character limit 255', max_length=255, verbose_name='Brands'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppagemodel',
            name='Ex_Tax',
            field=models.CharField(default=django.utils.timezone.now, help_text='max character limit 255', max_length=255, verbose_name='ex tax'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppagemodel',
            name='Product_Code',
            field=models.CharField(default=django.utils.timezone.now, help_text='max character limit 255', max_length=255, verbose_name='Product Code '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppagemodel',
            name='Reward_Points',
            field=models.CharField(default=django.utils.timezone.now, help_text='max character limit 255', max_length=255, verbose_name=' Reward Points '),
            preserve_default=False,
        ),
    ]
