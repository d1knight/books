from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='description')
    slug = models.SlugField(default="", null=False)
    def __str__(self):
        return self.name

