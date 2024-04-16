from django.contrib.auth.models import AbstractUser
from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='tours/')


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    number_of_people = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
