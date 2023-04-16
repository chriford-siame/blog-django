# Generated by Django 3.2 on 2023-03-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("security", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                max_length=255, null=True, verbose_name="first_name"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=255, null=True, verbose_name="last_name"),
        ),
    ]
