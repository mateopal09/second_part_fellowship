# Generated by Django 4.2.7 on 2023-11-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_stories_feature', '0007_delete_querymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=200)),
                ('series_code', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
            ],
        ),
    ]