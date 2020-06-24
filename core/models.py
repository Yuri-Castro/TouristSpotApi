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
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.name

