# Generated by Django 3.2.16 on 2022-12-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topy', '0006_match_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address line 2'),
        ),
    ]
