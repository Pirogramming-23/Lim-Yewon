from django.db import models

# Create your models here.

class Post(models.Model) :
    user_id = models.CharField(max_length=50, default='이름없음')
    content = models.TextField()
    like = models.IntegerField()
    photo = models.ImageField('이미지', blank=True, upload_to='images/%Y%m%d')

class Comment(models.Model) :
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)