# Generated by Django 5.1.7 on 2025-03-07 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='command',
            new_name='order',
        ),
    ]
