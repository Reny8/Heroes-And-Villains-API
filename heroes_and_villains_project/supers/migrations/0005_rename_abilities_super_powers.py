# Generated by Django 4.0.3 on 2022-04-05 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0004_remove_super_primary_ability_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='abilities',
            new_name='powers',
        ),
    ]
