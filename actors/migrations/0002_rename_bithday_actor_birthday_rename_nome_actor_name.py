# Generated by Django 5.0.4 on 2024-05-17 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("actors", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="actor",
            old_name="bithday",
            new_name="birthday",
        ),
        migrations.RenameField(
            model_name="actor",
            old_name="nome",
            new_name="name",
        ),
    ]
