# Generated by Django 4.1.7 on 2023-02-18 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hello_world", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HelloWorldMessages",
            new_name="HelloWorldMessage",
        ),
    ]
