from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Restaurante(models.Model):
    id = models.CharField(primary_key=True, blank=False, null=False, max_length=64)
    rating = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    name = models.CharField(max_length=100, blank=True, null=False)
    site = models.CharField(max_length=100, blank=True, null=False)
    email = models.EmailField(max_length=100, blank=True, null=False)
    phone = models.CharField(max_length=100, blank=True, null=False)
    street = models.CharField(max_length=100, blank=True, null=False)
    city = models.CharField(max_length=100, blank=True, null=False)
    state = models.CharField(max_length=100, blank=True, null=False)
    lat = models.CharField(max_length=100, blank=True, null=False)
    lng = models.CharField(max_length=100, blank=True, null=False)
