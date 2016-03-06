from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField()
    body = models.TextField()
    url = models.URLField()
