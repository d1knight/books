from django.db import models
from django.utils.text import slugify

class Authors(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, default='No description', blank=True, null=True)
    slug = models.SlugField(default="", null=False)
    banner = models.ImageField(default="Гоголь.jpg", blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name