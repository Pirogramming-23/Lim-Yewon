from django.db import models

categories = [
    ("멜로/로맨스", "멜로/로맨스"),
    ("액션", "액션"),
    ("스릴러", "스릴러"),
    ("코미디", "코미디"),
    ("판타지", "판타지"),
    ("SF", "SF"),
    ("범죄", "범죄"),
    ("전쟁", "전쟁"),
    ("스포츠", "스포츠"),
    ("음악/뮤지컬", "음악/뮤지컬"),
    ("드라마", "드라마"),
    ("애니메이션", "애니메이션"),
]

# Create your models here.
class Review(models.Model) :
    title = models.CharField(max_length=40)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=20, choices=categories)
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    director = models.CharField(max_length=40, null=True, blank=True)
    actors = models.CharField(max_length=40, null=True, blank=True)
    running_time = models.PositiveBigIntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)