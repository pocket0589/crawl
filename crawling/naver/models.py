from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255)
    time = models.DateTimeField(blank=True, null=True)
    body = models.TextField()
    url = models.URLField()

    author = models.ManyToManyField('Author', related_name='articles', blank=True, null=True)
    publisher = models.ForeignKey('Publisher', blank=True, null=True, on_delete=models.SET_NULL, related_name='articles')

    def __str__(self):
        return self.title


class Publisher(models.Model):

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='publishers/', blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL, related_name='authors')

    def __str__(self):
        return self.name
