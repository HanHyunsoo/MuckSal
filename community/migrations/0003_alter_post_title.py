# Generated by Django 3.2.5 on 2021-08-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20210803_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
