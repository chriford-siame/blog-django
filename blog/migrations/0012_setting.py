# Generated by Django 3.2 on 2023-03-15 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20230315_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('theme', models.CharField(blank=True, choices=[('dark', 'Dark'), ('light', 'Light')], default='dark', max_length=200, null=True, unique=True)),
                ('default_category', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='Default Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
