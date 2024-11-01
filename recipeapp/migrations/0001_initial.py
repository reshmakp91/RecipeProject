# Generated by Django 4.2.16 on 2024-10-04 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Prep_time', models.DurationField(default=datetime.timedelta(seconds=7200))),
                ('Difficulty', models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])),
                ('Vegetarian', models.BooleanField()),
                ('Recipe_img', models.ImageField(upload_to='recipe/')),
                ('Description', models.CharField(max_length=5000)),
            ],
        ),
    ]
