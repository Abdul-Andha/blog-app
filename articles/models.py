from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=128)
  slug = models.SlugField(max_length=128)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  thumbnail = models.ImageField(default='default.png', blank=True)
  #author
  #word count / char count

  def __str__(self):
    return self.title

  def snippet(self):
    return self.body[:50] + "..."