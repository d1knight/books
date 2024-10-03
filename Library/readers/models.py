from django.db import models


class Readers(models.Model):  # connect with Booking
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    image = models.ImageField(default="Test.jpg", blank=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name
