# Generated by Django 4.1.2 on 2022-10-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_rename_facts_fact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('volume', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='freelance',
            field=models.CharField(choices=[('Not Available', 'false'), ('Available', 'true')], default='true', max_length=20),
        ),
    ]