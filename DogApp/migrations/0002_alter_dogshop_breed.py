# Generated by Django 4.1.7 on 2023-07-20 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogshop',
            name='breed',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
