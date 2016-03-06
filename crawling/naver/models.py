from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    body = models.TextField()
    url = models.URLField()

    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL, related_name='articles')
    publisher = models.ForeignKey('Publisher', blank=True, null=True, on_delete=models.SET_NULL, related_name='articles')

    def __str__(self):
        return self.title


class Publisher(models.Model):

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='publishers/')

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
