from django.db import models
import datetime
from datetime import datetime, time
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=21, default="", blank=False)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=14, blank=False, default="Vlad")

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=30, default="", blank=False)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField(default=0)
    duration = models.TimeField(default=time(1, 2, 3, 0))
    description = models.TextField(default="<blank>")
    photo = models.ImageField(upload_to="film_photos", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('film_details', args=[str(self.id)])

    def __str__(self):
        return self.name


class CountDown(models.Model):
    session = models.CharField(max_length=50, unique=True,null=True,blank=True)
    start_time = models.DateTimeField(default=datetime.now())
    duration = models.IntegerField(default=0)


class Coupon(models.Model):
    code = models.CharField(max_length=15,default="nov")
    discount = models.DecimalField(max_digits=3,decimal_places=1)
    is_active = models.BooleanField(default=True)