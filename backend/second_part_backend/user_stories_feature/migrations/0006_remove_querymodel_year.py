# Generated by Django 4.2.7 on 2023-11-14 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_stories_feature', '0005_alter_querymodel_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='querymodel',
            name='year',
        ),
    ]
