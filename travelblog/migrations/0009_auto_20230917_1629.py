# Generated by Django 3.2.20 on 2023-09-17 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0008_auto_20230917_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_first_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_last_name',
        ),
    ]
