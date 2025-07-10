from django.db import models

# Create your models here.
class Review(models.Model) :
    title = models.CharField(max_length=40)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=20)
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    director = models.CharField(max_length=40, null=True, blank=True)
    actors = models.CharField(max_length=40, null=True, blank=True)
    running_time = models.PositiveBigIntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)