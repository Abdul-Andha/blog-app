from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=128)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  #thumbnail
  #author
  #word count / char count