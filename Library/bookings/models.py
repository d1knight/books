from django.db import models

from personal.models import Personal
from readers.models import Readers
from Books.models import Books


class Booking(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    readers = models.ForeignKey(Readers, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    getDate = models.DateField()
    returnDate = models.DateField()
    slug = models.SlugField(default='', null=False)
    def __str__(self):
        return f'{self.personal} |--------------------| {self.readers}'
