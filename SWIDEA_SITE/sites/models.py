from django.db import models
from django.contrib.auth.models import User
from devtools.models import DevTool

devtools = [
    ("HTML", "HTML"),
    ("CSS", "CSS"),
    ("JavaScript", "Javascript"),
    ("Django", "Django"),
]

# Create your models here.
class Idea(models.Model) :
    title = models.CharField(max_length=40)
    content = models.TextField()
    interest = models.BigIntegerField()
    devtool = models.ForeignKey(DevTool, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField('이미지', blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Idea, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f"{self.user.username} - {self.item.title}"