# Generated by Django 4.1.3 on 2022-11-13 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("topy", "0002_alter_activity_activity_id_alter_child_child_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="seniorcitizen", name="birthday",),
        migrations.RemoveField(model_name="seniorcitizen", name="gender",),
        migrations.RemoveField(model_name="seniorcitizen", name="name",),
    ]
