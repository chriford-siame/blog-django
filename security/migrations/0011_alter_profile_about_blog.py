# Generated by Django 3.2 on 2023-04-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0010_profile_about_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_blog',
            field=models.TextField(blank=True, null=True, verbose_name='About Blog'),
        ),
    ]
