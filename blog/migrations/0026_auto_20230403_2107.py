# Generated by Django 3.2 on 2023-04-03 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='trash',
            options={'ordering': ['-pk']},
        ),
    ]