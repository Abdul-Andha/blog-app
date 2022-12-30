from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=128)
  slug = models.SlugField(max_length=128)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  thumbnail = models.ImageField(default='default.png', blank=True)
  author = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)
  wordCount = models.IntegerField(default=0)

  def __str__(self):
    return self.title

  def snippet(self):
    return self.body[:100] + "..."

  def readingTime(self):
    time = int(self.wordCount / 238 * 60)
    minutes = time // 60
    seconds = time % 60
    return f"{minutes} min {seconds} sec"