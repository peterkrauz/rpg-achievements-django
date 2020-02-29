from django.db import models


class Rpg(models.Model):
    title = models.TextField(max_length=256, default='')
    description = models.TextField(max_length=512, default='')
    created_at = models.DateField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.title
