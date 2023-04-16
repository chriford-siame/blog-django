# Generated by Django 3.2 on 2023-04-03 21:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("security", "0004_user_is_first_time_login"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True, max_length=25, null=True, verbose_name="Country"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="state",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="State/Province"
            ),
        ),
    ]
