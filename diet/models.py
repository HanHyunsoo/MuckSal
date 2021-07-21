from django.db import models


# Create your models here.
# 식판 클래스
class Food(models.Model):
    CATEGORY_CHOICES = (
        ('01', "밥"),
        ('02', '국'),
        ('03', '반찬')
    )

    food_name = models.CharField(max_length=50)
    food_image = models.ImageField(blank=True, upload_to="food/")
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    protein = models.IntegerField()
    carbohydrate = models.IntegerField()
    fat = models.IntegerField()
    calorie = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField('diet.FoodHashtag', related_name="hashtags", blank=True)

    def __str__(self):
        return self.food_name


class FoodHashtag(models.Model):
    content = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class MealPlanner(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='users')
    foods = models.ManyToManyField('diet.Food', related_name='foods')
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s의 식단(%s)" % (self.user.username, self.reg_date)