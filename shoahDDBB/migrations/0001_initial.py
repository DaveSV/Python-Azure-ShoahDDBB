# Generated by Django 4.0.6 on 2022-07-31 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mov_name', models.CharField(max_length=50)),
                ('mov_year', models.CharField(max_length=4)),
                ('mov_country', models.CharField(max_length=30)),
                ('mov_director', models.CharField(max_length=50)),
                ('mov_language', models.CharField(max_length=20)),
                ('mov_overview', models.TextField()),
                ('url_movie', models.CharField(max_length=50)),
                ('url_trailer', models.CharField(max_length=50)),
                ('mov_poster', models.CharField(max_length=50)),
                ('mov_streaming', models.CharField(max_length=50)),
            ],
        ),
    ]