# Generated by Django 4.2.1 on 2023-06-06 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
