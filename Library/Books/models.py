from django.db import models

from authors.models import Authors
from genres.models import Genres


class Books(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    authors = models.ManyToManyField(Authors, blank=True)
    genres = models.ManyToManyField(Genres, blank=True)
    slug = models.SlugField(default="", null=False)
    description = models.TextField(default="")
    publishingYear = models.PositiveIntegerField(default=1) 
    price = models.CharField(max_length=20, default='0.00')
    publication = models.CharField(max_length=100, default="no_publication")
    binding = models.CharField(max_length=50, default='no_binding')

    def __str__(self):
        return self.name
