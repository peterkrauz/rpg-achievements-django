from django.db import models
from rpgs.models import Rpg


class Achievement(models.Model):
    title = models.TextField(max_length=256)
    rpg_id = models.ForeignKey(Rpg, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=512)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
