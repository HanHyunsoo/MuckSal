# Generated by Django 3.2.6 on 2021-08-13 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50, unique=True)),
                ('food_image', models.ImageField(blank=True, upload_to='food/')),
                ('category', models.CharField(choices=[('01', '밥'), ('02', '국'), ('03', '반찬')], max_length=2)),
                ('protein', models.IntegerField()),
                ('carbohydrate', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('calorie', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodHashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=20)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('foods', models.ManyToManyField(related_name='foods', to='diet.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='hashtags',
            field=models.ManyToManyField(blank=True, related_name='hashtags', to='diet.FoodHashtag'),
        ),
    ]
