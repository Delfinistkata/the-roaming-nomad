# Generated by Django 3.2.20 on 2023-07-16 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0002_alter_post_post_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
