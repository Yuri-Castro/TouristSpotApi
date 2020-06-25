from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from address.models import Address


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,\
                                blank=True, null=True)
    photo = models.ImageField(upload_to='touristspots', blank=True, null=True)

    def __str__(self):
        return self.name

