from django.db import models


class Personal(models.Model):  # connect with Booking
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100, default='position')
    photo = models.ImageField(default="Test.jpg", blank=True)
    adress = models.CharField(max_length=50, default='adress')
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.name
