from django.db import models
from datetime import timedelta

class Recipes(models.Model):

    Name = models.CharField(max_length=200)
    Prep_time = models.DurationField(default=timedelta(minutes=0))
    Difficulty_choices = [(1,'Easy'),(2,'Medium'),(3,'Hard')]
    Difficulty = models.IntegerField(choices=Difficulty_choices)
    Vegetarian = models.BooleanField()
    Recipe_img = models.ImageField(upload_to='recipe/',null=True, blank=True)
    Description = models.CharField(max_length=1000,null=True)
    Ingredients = models.TextField(null=True)
    Instructions = models.TextField(null=True)

