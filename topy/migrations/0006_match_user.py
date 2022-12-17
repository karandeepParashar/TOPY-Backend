# Generated by Django 4.1.3 on 2022-12-04 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("topy", "0005_activity_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="match",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="topy.user"
            ),
            preserve_default=False,
        ),
    ]