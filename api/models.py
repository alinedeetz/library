from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=256)
    number_of_pages = models.IntegerField()
    author = models.CharField(max_length=50)
    
class ReadingList(models.Model):
    book = models.CharField(max_length=256)

class Movies(models.Model):
    movie = models.CharField(max_length=256)