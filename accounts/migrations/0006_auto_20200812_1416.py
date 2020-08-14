# Generated by Django 3.1 on 2020-08-12 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200812_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_superadmin',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='phone'),
        ),
    ]