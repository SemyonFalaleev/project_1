from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=False)

class Hotel(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    street_number = models.CharField(max_length=100, null=False)

class HotelRoom(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="room"

    )
    description = models.TextField(null=False)
    number_room = models.IntegerField(unique=False, null=False)

class RoomReservation(models.Model):
    hotel_room = models.ForeignKey(
        HotelRoom, 
        on_delete=models.CASCADE,
        related_name="reservation"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservation"
    )
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=False)
