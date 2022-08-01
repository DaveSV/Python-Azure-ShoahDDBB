# Generated by Django 4.0.6 on 2022-07-31 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoahDDBB', '0004_movies_mov_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='mov_rating',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default='PG', max_length=5, null=True),
        ),
    ]
