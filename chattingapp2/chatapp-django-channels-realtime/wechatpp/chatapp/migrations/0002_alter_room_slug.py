# Generated by Django 4.2.1 on 2023-05-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
