# Generated by Django 4.1.2 on 2022-10-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_profile_freelance_profile_profession_profile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='freelance',
            field=models.CharField(choices=[('Available', 'true'), ('Not Available', 'false')], default='true', max_length=20),
        ),
    ]
