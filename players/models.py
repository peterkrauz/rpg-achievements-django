from django.db import models
from achievements.models import Achievement


class Player(models.Model):
    name = models.TextField(max_length=256)
    achievements = models.ManyToManyField(Achievement)
    email = models.EmailField(max_length=128, default="default@gmail.com")
    password = models.TextField(max_length=64, default="12345")

    def __str__(self):
        return self.name
