# Generated by Django 4.1.2 on 2022-10-29 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_facts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Facts',
            new_name='Fact',
        ),
    ]
