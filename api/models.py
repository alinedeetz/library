from django.db import models
from datetime import now

class Books(models.Model):
    name = models.CharField(max_length=256)
    number_of_pages = models.IntegerField()
    author = models.CharField(max_length=50)
    read_date = models.DateTimeField()
    