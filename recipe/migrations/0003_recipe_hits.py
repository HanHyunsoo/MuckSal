# Generated by Django 3.2 on 2021-11-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
