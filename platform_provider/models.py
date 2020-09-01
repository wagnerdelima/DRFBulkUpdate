from django.db import models

# Create your models here.


class PlatformProvider(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    kind = models.CharField(max_length=100, default='casino')

    def __str__(self):
        return f'{self.id} - {self.name}'
